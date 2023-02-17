from re import escape
from string import ascii_lowercase, ascii_uppercase, digits

LONG_LINK_CHAR_LIMIT = 10190
RANDOM_ID_ITERATIONS = 10
RANDOM_LINK_LENGTH = 6
SHORT_LINK_CHAR_LIMIT = 16

VALID_CHARACTER_SEQUENCE = ascii_lowercase + ascii_uppercase + digits
VALID_CHARACTERS_PATTERN = fr'^[{escape(VALID_CHARACTER_SEQUENCE)}]*$'

OUT_OF_LUCK = (
    'Все возможные комбинации исчерпаны, '
    'или заданное количество попыток слишком мало')

SUBMIT_BUTTON_LABEL = 'Создать'
ORIGINAL_LINK_LABEL = 'Длинная ссылка'
CUSTOM_ID_LABEL = 'Ваш вариант короткой ссылки'
REQUIRED_FIELD = 'Обязательное поле'
INVALID_URL_STRING = 'Введённая строка не соответствует формату URL'
INCORRECT_STRING_LENGTH = ('Принимается строка длиной до '
                           '{limit} символов включительно')
INVALID_CHARACTERS = ('Использованы недопустимые символы. '
                      'Допустимые символы: латинские буквы и цифры')

BASE_API_ERROR = 'Ошибка валидации: {error_message}'
DOESNT_EXIST = 'Указанный id не найден'
EMPTY_REQUEST = 'Отсутствует тело запроса'
FIELDS_MISSING = '"{field}" является обязательным полем!'
INVALID_URL_FORMAT = '"{url}" не является валидным URL'
DUPLICATE_SHORT_LINK = 'Имя {short_link} уже занято{end}'
INVALID_SHORT_LINK = 'Указано недопустимое имя для короткой ссылки'
