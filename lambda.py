import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)





# lambda_handler defined in aws as function to invoke.
def lambda_handler(event, context):
    try:
      arguments = validate_arguments(event)
      response = buildResponse(arguments)
      return response
    except Exception as e:
      raise e




# functions called by entry function
def validate_arguments(params):
    logger.debug(params)
    name = params['name']
    if name != "eddie":
        logger.error("Request token (%s) does not match exptected", token)
        raise Exception("Invalid request token")

    arguments = {}
    if 'name' not in params:
        logger.error("no Name provided")
        raise Exception("You must provide a name!")      
    arguments['name'] = params['name'].strip()
    return arguments



#print response
def buildResponse(arguments):
  response = {
    "message": "hello " + arguments['name']
  }
  return response      





if __name__ == '__main__':
  
  """Test that error returned if token does not match expected"""
  event = {"notname" : "somestring" }  
  try:
    start = time.time()
    result = lambda_handler(event,None)
    raise Exception("Test failed, accepts invalid input")
  except Exception as e:
    end = time.time()
    print("--- %s seconds ---" % (end - start))
    if "name" in str(e):
      print("Pass")  
    else: 
      print("Error"+str(e))

  """Test that a response is returned with valid token"""  
  event = {
    "name" : "eddie"
    } 
  start = time.time()
  result = lambda_handler(event,None)
  end = time.time()
  print("--- %s seconds ---" % (end - start))
  if "hello eddie" not in str(result):
    print(result)
    raise Exception("Test failed, expected valid response")
  else:
    print("Pass")  


    
