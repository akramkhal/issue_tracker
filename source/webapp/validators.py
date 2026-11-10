from django.core.exceptions import ValidationError


def validate_capitalized(value):
    if not value[0].isupper():
        raise ValidationError('Краткое описание должно начинаться с заглавной буквы.')


def validate_min_length(value):
    if len(value.strip()) < 10:
        raise ValidationError('Полное описание должно содержать не менее 10 символов.')