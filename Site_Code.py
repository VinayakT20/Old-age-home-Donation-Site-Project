import re
def payment_gateway():
     if payment_option==1:
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\tWelcome to Payment Gateway!\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         credit=int(input("Enter Credit card number: "))
         while (999999999999999>credit) or (credit>10000000000000000):
             print("ERROR! ENTER 16 DIGIT CREDIT CARD NUMBER ONLY!")
             credit=int(input("Enter Credit card number: "))
         credit_expiry_date = input("Enter Expiry date (mm/yy): ")
         x = re.search("[0-1][1-9]/[2-9][2-9]", credit_expiry_date)
         if x:
             pass
         else:
             print("ERROR! Enter EXPIRY DATE IN (MM/YY) FORMAT!")
             credit_expiry_date = input("Enter Expiry date (mm/yy): ")
         cvv=int(input("Enter CVV Code: "))
         while (99>cvv) or (cvv>1000):
             print("ERROR! ENTER 3 DIGIT CVV CODE!")
             cvv=int(input("Enter CVV Code: ")) 
 
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t   Please wait a second.\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         print(f"OTP has been sent to you number '{last_four_digit_number}'." )
         credit_otp=int(input("Enter OTP: "))
         while (99999>credit_otp) or (credit_otp>1000000):
             print("ERROR! ENTER 6 DIGIT OTP ONLY!")
             credit_otp=int(input("Enter OTP: "))
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t   Please wait a second.\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t    Payment Successful\t\t\t\t\t\t  |")
         print("|\t\t\t\t  Redirecting to website\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")


     elif payment_option==2:
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\tWelcome to Payment Gateway!\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         debit_card_number=int(input("Enter Debit card number: "))
         while (999999999999999>debit_card_number) or (debit_card_number>10000000000000000):
             print("ERROR! ENTER 16 DIGIT CREDIT CARD NUMBER ONLY!")
             debit_card_number=int(input("Enter Debit card number: "))
         debit_expiry_date = input("Enter Expiry date: ")
         y = re.search("[0-1][1-9]/[2-9][2-9]", debit_expiry_date)
         if y:
             pass
         else:
             print("ERROR! Enter EXPIRY DATE IN (MM/YY) FORMAT!")
             debit_expiry_date = input("Enter Expiry date: ")

         debit_cvv_number = int(input("Enter CVV Code: "))
         while (99>debit_cvv_number) or (debit_cvv_number>1000):
             print("ERROR! ENTER 3 DIGIT CVV CODE!")
             debit_cvv_number=int(input("Enter CVV Code: ")) 
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t   Please wait a second.\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         print(f"OTP has been sent to you number {last_four_digit_number}." )
         debit_otp=int(input("Enter OTP: "))
         while (99999>debit_otp) or (debit_otp>1000000):
             print("ERROR! ENTER 6 DIGIT OTP ONLY!")
             debit_otp=int(input("Enter OTP: "))
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t   Please wait a second.\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t    Payment Successful\t\t\t\t\t\t  |")
         print("|\t\t\t\t  Redirecting to website\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")


def QNA():
            
     a=input("Would you like to solve your query ?(Y/N):")
     if(a=="y") or (a=="Y"):
         op1=int(input("Having problem in making account? Press 0 : "))
         if(op1==0):
             print("Contact us on our website ")
         else:
             print("Thank you")
         print("\n")
         op2=int(input("To know our website is secure? Press 1 : "))
         if (op2==1):
             print("Yes ! Our website is secured with high level security system ")
         else:
             print("Thank you")
         print("\n")
         op3=int(input("Having any financial query ?  Press 3 : "))
         if(op3==3):
             print("Contact on 562134562")
         else:
             print("Thank you")
         print("\n")
         op4=int(input("Problem on how to donate ? Press 4 : "))
         if(op4==4):
             print("You can donate online or for more details contact 2346598702")
         else:
             print("Thank you")
         print("\n")
         op5=int(input("Would you like to join with us ? Press 5 : "))
         if(op5==5):
             print("Contact our member Mr X - 2365178452")
         else:
             print("Thank you")
         print("\n")
         print("For any other query Contact us on phn no. 9999988845 or mail us on donation")
     else:          
         print("Thank you")

def e_mail():
    
    import os #provides functions for interacting with the operating system.
    from email.message import EmailMessage
    import ssl #provides secure connection
    import smtplib #module to send mail
    from email.utils import formataddr
    from pathlib import Path

    email_sender= 'donation.practical@gmail.com'
    email_password= 'shrdbicqaifalnih'
    email_receiver= donor_mail

    subject = "Donation"


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content('xyz')
    #HTML Code
    em.add_alternative("""\
    <DOCTYPE! html>
    <html lang="en">
            <head>
                <style>
                    h1 {color: black;text-align: center;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;}
                    footer {text-align: center;}
                    img {width: 300px; height: 105px}
                    .center {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 50%;
                    }
                </style>
            </head>
            <body>
                <a href="https://www.helpageindia.org/" target="_blank">
                <img src="https://www.helpageindia.org/wp-content/uploads/2021/09/HelpAge-India-LOGO.jpg" class="center">
                </a>
                <h1><b>HelpAge India</b></h1>
                <hr>
                Thank you for donating! We appreciate it. <br><br>

                80G Certificate will be sent to you soon on your mail box.<br><br>
                Meanwhile, you can know more about us and our mission.<br><br>
                HelpAge India is a secular, not-for-profit organization in India, registered under the Societies’ Registration Act of 1860. Set up in 1978, the organization works for ‘the cause and care of disadvantaged older persons to improve their quality of life’ HelpAge envisions a society where elderly have the right to an active, healthy and dignified life. It recently became the first and only Indian organization to be honoured with the ‘UN Population Award 2020’ for its exemplary work in the field of ageing, relief efforts work during the Covid 19 pandemic and recognition of the organization’s outstanding contribution to population issues and efforts in the realization of older persons rights in India.<br><br>
                HelpAge India is able to carry out its work on ground due to the generosity of its donors. Its largest supports are individuals who donate to the elder cause from their hard-earned money. Among them are also school children who want to make a difference and are motivated by teachers and parents, to do their bit for the elderly. On the other hand, Corporate Social Responsibility has increased over the years with more and more companies now choosing to do their bit for society. Companies donate in various ways – the foremost being supporting our projects in ground such as donating and supporting the running costs of our Mobile Healthcare Units, sponsoring cataract surgeries and our Support a Gran program among others. Other ways of support are through Cause Related Marketing, and Payroll Giving initiatives, even donating in kind.<br><br>
                HelpAge also receives wide support from various Trusts & Foundations across the country.

                <hr>
                <footer>
                    © 2017 HelpAge NGO in India-Non Profit Organization - All Rights Reserved.
                </footer>
                <hr>
            </body>
        </html>

    """, subtype='html')
    ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password) #login credentials
        smtp.sendmail(email_sender, email_receiver, em.as_string())



print("---------------------------------------------------------------------------------------------------")
print("|\t\t\t\t\tHelpAge Foundation!\t\t\t\t\t  |")
print("|\t\t\t\t\t Help for Elders\t\t\t\t\t  |")
print("---------------------------------------------------------------------------------------------------")





print("---------------------------------------------------------------------------------------------------")
print("|\t\t\t\t\t    Welcome!\t\t\t\t\t\t  |")
print("---------------------------------------------------------------------------------------------------")
log_in=input("Press '1' to sign up or press '2' to sign in: ")
while log_in!='1' and log_in!='2':
    print("Error! Press '1' or '2' only!")
    log_in=input("Press '1' to sign up or press '2' to sign in: ")
import re
if log_in=="1":
    print("---------------------------------------------------------------------------------------------------")
    print("|\t\t\t\t\tWelcome!\t\t\t\t\t\t  |")
    print("---------------------------------------------------------------------------------------------------")
    username=input("Enter Username: ")
    password1=input("Enter Password: ")
    password2=input("Enter Password again to confirm: ")
    while password1!=password2:
        print("Password not matching!")
        password1=input("Enter Password: ")
        password2=input("Enter Password again to confirm: ")
    if password1==password2:
         print(f"Welcome {username}!")
         print("---------------------------------------------------------------------------------------------------")
         print("|\t\t\t\t\tDONOR DETAILS\t\t\t\t\t\t  |")
         print("---------------------------------------------------------------------------------------------------")
         contact_no=int(input("Enter Mobile number:"))
         while (999999999>contact_no) or (contact_no>10000000000):
             print("ERROR! ENTER 10 DIGIT ONLY!")
             contact_no=int(input("Enter Mobile number:"))

         donor_mail=input("Enter Mail ID: ") #Use Real Email
         var ="@gmail.com"
         if (donor_mail=="^[a-zA-Z0-9_\-\.]+[@][a-z]+^[\.][a-z]{2,3}"):
              pass
         else:
             print("Sorry!ENTER CORRECT EMAIL!")
             donor_mail=input("Enter Mail ID: ")
         address= input("Enter Address: ")
         last_four_digit_number=contact_no%10000
         payment_option=int(input("Enter Payment Option (press 1 for credit card or 2 for debitcard): "))
         while payment_option!=1 and payment_option!=2:
             print("Invalid Choice! Press '1' or '2 only'")
             payment_option=int(input("Enter Payment Option (press 1 for credit card or 2 for debitcard): "))
         if payment_option==1 or payment_option==2:
             payment_gateway()
             print("|\t\t\t\t   Payment Successful\t\t\t\t\t\t   |")
             print("|\t\t\t\tA mail has been sent to you!\t\t\t\t\t   |")
             print("---------------------------------------------------------------------------------------------------")
             e_mail()
             QNA()
        

  
elif log_in=="2":
     
     print("Welcome!")
     username = "Vinayak"
     password = "1234"
     user = input("Enter Username:")
     pas= input("Enter Password:")

     while (user != username) and (pas != password):
            print("ERROR! INVALID CREDENTIALS!")
            user = input("Enter Username:")
            pas= input("Enter Password:")
     if (user==username and pas==password):
         print("Login successful\n")

         donate_inp= input("Do you want to donate Y/N:")

         while donate_inp!="Y" and donate_inp!="y" and donate_inp!="N" and donate_inp!="n":
             print("Press only 'Y' or 'N': ")
             donate_inp= input("Do you want to donate Y/N:")

         if donate_inp=="Y" or donate_inp=="y":
             print("")

             name= input("Enter Your Name:\n")
             

             contact_no= int(input("Enter Contact Number:\n"))
             while (999999999>contact_no) or (contact_no>10000000000):
                 print("ERROR! ENTER 10 DIGIT ONLY!")
                 contact_no=int(input("Enter Mobile number:"))
             

             locality= input("Enter Your Locality:\n")
             

             donor_mail=input("Enter Mail ID: \n") #Put original mail ID for result
             var ="@gmail.com"
             if (donor_mail=="^[a-zA-Z0-9_\-\.]+[@][a-z]+^[\.][a-z]{2,3}"):
                 pass
             else:
                 print("Sorry!ENTER CORRECT EMAIL!")
                 donor_mail=input("Enter Mail ID: ")
             


             last_four_digit_number=contact_no%10000
             payment_option=int(input("Enter Payment Option (press 1 for credit card or 2 for debitcard): "))
             while payment_option!=1 and payment_option!=2:
                 print("Invalid Choice! Press '1' or '2 only'")
                 payment_option=int(input("Enter Payment Option (press 1 for credit card or 2 for debitcard): "))
             if payment_option==1 or payment_option==2:
                 payment_gateway()
                 print("|\t\t\t\t   Payment Successful\t\t\t\t\t\t   |")
                 print("|\t\t\t\tA mail has been sent to you!\t\t\t\t\t   |")
                 print("---------------------------------------------------------------------------------------------------")
                 e_mail()
                 QNA()

         elif donate_inp=="N" or donate_inp=="n":
            print("Thank You! Visit Again!")
         
        



    

