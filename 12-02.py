def details(**kargs):
    for i,j in kargs.items():
        print(i,j,sep=" : ")

details(user_name = 'Madhu', user_pw = '@123', user_dob = '12-34-56' )
details(user_name = 'Manisha', user_pw = '@1234', remarks = 'Good')
