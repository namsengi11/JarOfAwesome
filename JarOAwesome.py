import datetime
import random

class Jar:
  def __init__(self) -> None:
    self.eventList = []

  def addEvent(self):
    event = Event.createEvent()
    self.eventList.append(event)

  def drawEvent(self):
    if not self.eventList:
        print("No awesome events to draw. Add some first!")
        return None

    index = random.randrange(0, len(self.eventList))
    return self.eventList[index]

  def __str__(self) -> str:
    result = ""
    counter = 1
    for event in self.eventList:
      result += str(counter) + ". " + str(event) + "\n"
      counter += 1
    return result

class Event:
  def __init__(self, title, content, date) -> None:
    self.title = title
    self.content = content
    self.date = date

  def __str__(self) -> str:
    return self.date + "\n" + self.title + ": " + self.content + '\n'

  @classmethod
  def createEvent(cls):
    eventTitle = input("What's something awesome that happened today?\n")
    print("\n")
    eventSummary = input("Provide a brief overview of what happened :D\n")
    print("\n")
    eventTime = str(datetime.datetime.now())[:16]
    return cls(eventTitle, eventSummary, eventTime)

myJar = Jar()

while True:
  userInput = input("What would you like to do? Enter one of the following\n" +
    "1. Enter \"add\" to add new awesome event\n" +
    "2. Enter \"draw\" to revisit one awesome event that happened to me\n" +
    "3. Enter \"view\" to view all awesome events that ever happened to me\n\n")
  print("\n")

  if userInput == "add":
    myJar.addEvent()
    print("Awesome event successfully added!\n")
  elif userInput == "draw":
    print("Here's one awesome event that you can go back to!\n")
    print(myJar.drawEvent())
  elif userInput == "view":
    print(str(myJar))
  else:
    print("Unknown input! Try again!\n")


