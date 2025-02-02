from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
from deep_translator import GoogleTranslator
import time

class FAQ(models.Model):
    # English (Default)
    question = models.TextField(verbose_name='Question (English)')
    answer = RichTextField(verbose_name='Answer (English)')
    
    # Hindi
    question_hi = models.TextField(verbose_name='Question (Hindi)', blank=True)
    answer_hi = RichTextField(verbose_name='Answer (Hindi)', blank=True)
    
    # Bengali
    question_bn = models.TextField(verbose_name='Question (Bengali)', blank=True)
    answer_bn = RichTextField(verbose_name='Answer (Bengali)', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def translate_text(self, text, dest_lang):
        """Helper function to translate text with retries"""
        if not text:
            return ""
        
        # Clean the text by removing HTML tags for translation
        clean_text = strip_tags(text)
        print(f"Translating text to {dest_lang}: {clean_text}")
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                translator = GoogleTranslator(source='en', target=dest_lang)
                # Add a small delay to avoid rate limiting
                time.sleep(1)
                result = translator.translate(clean_text)
                if result:
                    print(f"Translation successful: {result}")
                    return result
            except Exception as e:
                print(f"Translation attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:  # Last attempt
                    print(f"All translation attempts failed for {dest_lang}")
                    return text  # Return original text if translation fails
                time.sleep(2)  # Wait before retrying
        return text

    def save(self, *args, **kwargs):
        # Check if this is a new object
        is_new = not self.pk
        
        # First save to ensure we have an ID
        super().save(*args, **kwargs)
        
        # Only translate for new objects or if translations are missing
        if is_new or not (self.question_hi and self.question_bn and self.answer_hi and self.answer_bn):
            try:
                print("Starting translations...")
                # Translate question if missing
                if not self.question_hi:
                    print("Translating question to Hindi...")
                    self.question_hi = self.translate_text(self.question, 'hi')
                if not self.question_bn:
                    print("Translating question to Bengali...")
                    self.question_bn = self.translate_text(self.question, 'bn')

                # Translate answer if missing
                if not self.answer_hi:
                    print("Translating answer to Hindi...")
                    self.answer_hi = self.translate_text(self.answer, 'hi')
                if not self.answer_bn:
                    print("Translating answer to Bengali...")
                    self.answer_bn = self.translate_text(self.answer, 'bn')

                # Save again with translations
                if is_new or any([
                    not self.question_hi,
                    not self.question_bn,
                    not self.answer_hi,
                    not self.answer_bn
                ]):
                    print("Saving translations...")
                    super().save(update_fields=['question_hi', 'question_bn', 'answer_hi', 'answer_bn'])
                    
            except Exception as e:
                print(f"Translation error: {str(e)}")
                # If translation fails, use English as fallback
                if not self.question_hi:
                    self.question_hi = self.question
                if not self.question_bn:
                    self.question_bn = self.question
                if not self.answer_hi:
                    self.answer_hi = self.answer
                if not self.answer_bn:
                    self.answer_bn = self.answer
                super().save(update_fields=['question_hi', 'question_bn', 'answer_hi', 'answer_bn'])

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question[:50]
