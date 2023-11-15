class Employee():
    def __init__(self,name,sales,bonus_hrs,base_salary) :
        self.name=name
        self.sales = sales
        self.bonus_hrs = bonus_hrs
        self.base_salary = base_salary
    

    def info(self):
        print("the employee name is :{}and the employeebase salary {} and sales are {}"
              .format(self.name,self.base_salary,self.sales))


#the main programe
emp1=Employee("azert",20000 , 42,30000)
emp2=Employee("asdfg",1500,74,15000)


emp1.info()
emp2.info()
  