from imageDetection.logger import logging
from imageDetection.exception import AppException
import sys
try:
    a =3/"s"

except Exception as e:
    raise AppException(e,sys)