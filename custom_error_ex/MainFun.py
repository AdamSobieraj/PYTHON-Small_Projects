from custom_error_ex.CustomError import CustomError
from custom_error_ex.DetailedError import DetailedError

# try:
#     raise CustomError("This is error message")
# except CustomError as e :
#     print(e.message)

try:
    raise DetailedError(error_code=404, description="Not Found")
except DetailedError as e :
    print(e.error_code)
    print(e.description)