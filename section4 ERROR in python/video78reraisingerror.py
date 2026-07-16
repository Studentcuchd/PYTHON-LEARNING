class user:
    def __init__(self,name,metrics):
        self.name=name
        self.metrics=metrics
        
    def __repr__(self):
        return f"User {self.name}"
    
# pass class obj as a parameter
def user_score(user):
    try:
        score= calculate(user.metrics)
    except KeyError:
        print("Please provide correct value ")
        raise
    #     # without re raise i donot knwo the actual error
        
        
# # we can handle this by 
#     except KeyError as e:
#         # print("Please provide correct value ")
#         # raise
#         # without re raise i donot knwo the actual error
#         print(e)

    else:
        print(send_noti(user.name))
        print(score)

# part2 finally and else
    finally:
        print("This is finally always runs")

    

        
        
def calculate(metrics):
    return metrics["clicks"]*5+metrics["hit"]*6


def send_noti(name):
    return f"notify user {name}"
    
user_obj=user("Parag",{"clicks": 10 , "hit": 4})

user_score(user_obj)




