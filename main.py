#TV PROJECT SCREEN
#
project_number = input("Enter Project Number: ")
job_number = input("Enter Job Number: ")
sales_number = input("Enter Sales Number: ")
customer_name = input("Enter Customer: ")
builder = input("Who is building the Project: ")
status = input("Status update: ")


print(f"""
-----------------------------------------------------------------------------------
      Project Number      Job Number      Sales Number     Customer Name      Builder      Status
|   {project_number:8}  {job_number:8}  {sales_number:8} {customer_name:30} {builder:10} {status:10} |
|   {project_number:8}  {job_number:8}  {sales_number:8} {customer_name:30} {builder:10} {status:10} |
|                                                                                  |
|                                                                                  |
-----------------------------------------------------------------------------------
""")