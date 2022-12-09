



class Ticket:
  ticket_num=0
  flight_code=""
  passenger_name=""
  date=""
  time=""
  seat_no=""


tickets =[]




while True :
  print("\n SELECT OPTION:")
  print("1.Delete ticket")
  print("2.Add ticket")
  print("3.List of tickets")
  print("4.Exit")
  option = int(input("\nEnter your option : "))

  if option == 4:
    print("Bye!")
    exit(0)

  if option == 1:
    ticket_num = int(input("\nTicket Number : "))
    for ticket in tickets:
        if ticket.ticket_num == ticket_num:
               tickets.remove(ticket)
               print("Ticket deleted!\n")

  if option == 2:
    ticket = Ticket()
    ticket.ticket_num = int(input("\nTicket Number : "))
    ticket.flight_code = str(input("\nFlight Code : "))
    ticket.passenger_name = str(input("\nName : "))
    ticket.date  = str(input("\nDate  : "))
    ticket.time  = str(input("\nTime : "))
    ticket.seat_no  = str(input("\nSeat Number : "))
    tickets.append(ticket)
    print("Ticket added!\n")

  if option == 3:
    for ticket in tickets:
       print("TICKET NUM | FLIGHT CODE | NAME | DATE | TIME| SEAT NO")
       print(str(ticket.ticket_num )+ " " + ticket.flight_code +" "+ticket.passenger_name+" "+ticket.date+" " +ticket.time+" "+ ticket.seat_no)

  
