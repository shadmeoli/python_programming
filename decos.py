
 # create a simple decorator
 
 
def loves(func: callable) -> callable:
 
    def  wrapper(*args, **kwargs)-> any:
