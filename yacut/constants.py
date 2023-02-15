from string import printable

SHORT_LINK_CHAR_LIMIT = 16
VALID_CHARACTER_SEQUENCE = printable[0:62]

ORIGINAL_LINK_LABEL = 'Длинная ссылка'
CUSTOM_ID_LABEL = 'Ваш вариант короткой ссылки'
REQUIRED_FIELD_MSG = 'Обязательное поле'
INVALID_URL_STRING_MSG = 'Введённая строка не соответствует формату URL'
INCORRECT_STRING_LENGTH_MSG = ('Принимается строка длиной до '
                               '{limit} символов включительно')
INVALID_CHARACTERS_MSG = ('Использованы недопустимые символы. '
                          'Допустимые символы: латинские буквы и цифры')

DOESNT_EXIST_MSG = 'Указанный id не найден'
EMPTY_REQUEST_MSG = 'Отсутствует тело запроса'
FIELDS_MISSING_MSG = '"{field}" является обязательным полем!'
INVALID_URL_FORMAT_MSG = '"{url}" не является валидным URL'
DUPLICATE_SHORT_LINK_MSG = 'Имя {short_link} уже занято{end}'
INVALID_SHORT_LINK_MSG = 'Указано недопустимое имя для короткой ссылки'
DEFAULT_OK_MSG = 'Ваша новая ссылка готова'