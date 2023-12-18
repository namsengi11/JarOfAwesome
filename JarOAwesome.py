import datetime
import random
import os.path

class Jar:
  def __init__(self) -> None:
    self.eventList = []

  @classmethod
  def createJar(cls):
    if not os.path.isfile("./storage.txt"):
      storage = open(r"storage.txt", "w")
      storage.close()
    storage = open(r"storage.txt", "r+")
    savedData = storage.readlines()
    newJar = Jar()
    for lineNo in range(1, len(savedData), 2):
      date, aweEvent = savedData[lineNo-1], savedData[lineNo]
      savedEvent = Event(aweEvent.split(": ")[0], aweEvent.split(": ")[1], date[:-1])
      newJar.addExistingEvent(savedEvent)
    storage.close()
    return newJar

  def addEvent(self):
    event = Event.createEvent()
    self.eventList.append(event)
    storage = open(r"storage.txt", "a")
    storage.write(str(event))
    storage.close()

  def takeEventIndex(self, index):
    while index >= len(self.eventList) or index < 1:
      print("Invalid index entered!\n")
      index = int(input("Enter the index of the awesome event!\n"))
    return index

  def editEvent(self, index):
    index = self.takeEventIndex(index)
    print(str(self.eventList[index-1]) + '\n')
    confirmation = input("Is this the event you'd like to edit? Press enter to continue editing.\n")
    if "" == confirmation:
      editingMode = True
      while editingMode:
        type = input("Which part (Title/Detail/Date) would you like to edit? Press enter to exit.\n").lower()
        typesAvail = {"title", "detail", "date"}
        if type in typesAvail:
          newInfo = input("Please enter new " + type + ".\n")
          self.eventList[index-1].editInfo(type, newInfo)
          print("\nAwesome event successfully edited!\n\n")
          editingMode = False
        if type == "":
          editingMode = False
        elif type not in typesAvail:
          print("Incorrect type entered. Try again.\n")

  def deleteEvent(self, index):
    index = self.takeEventIndex(index)
    print('\n' + str(self.eventList[index-1]))
    confirmation = input("Is this the event you'd like to delete? Press enter to confirm.\n")
    if confirmation == "":
      self.eventList.pop(index-1)

  def addExistingEvent(self, event):
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
  def __init__(self, title, detail, date) -> None:
    self.title = title
    self.detail = detail
    self.date = date

  def __str__(self) -> str:
    return self.date + "\n" + self.title + ": " + self.detail + '\n'

  @classmethod
  def createEvent(cls):
    eventTitle = input("What's something awesome that happened today?\n")
    print("\n")
    eventSummary = input("Provide a brief overview of what happened :D\n")
    print("\n")
    eventTime = str(datetime.datetime.now())[:16]
    return cls(eventTitle, eventSummary, eventTime)

  def editInfo(self, type, newInfo):
    if type == "title":
      self.title = newInfo
    elif type == "detail":
      self.detail = newInfo
    elif type == "date":
      self.detail = newInfo

myJar = Jar().createJar()

while True:
  userInput = input("What would you like to do? Enter one of the following\n" +
    "1. Enter \"add\" to add new awesome event :D\n" +
    "2. Enter \"edit\" to edit an awesome event in the jar\n" +
    "3. Enter \"delete\" to delete an awesome event in the jar ;(\n"
    "4. Enter \"draw\" to revisit one awesome event that happened to me :DD\n" +
    "5. Enter \"view\" to view all awesome events that ever happened to me\n\n")
  print("\n")

  if userInput == "add":
    myJar.addEvent()
    print("Awesome event successfully added!\n")
  elif userInput == "draw":
    print("Here's one awesome event that you can go back to!\n")
    print(myJar.drawEvent())
  elif userInput == "view":
    print(str(myJar))
  elif userInput == "edit":
    print(str(myJar))
    index = int(input("Enter the index of the awesome event!\n"))
    myJar.editEvent(index)
  elif userInput == "delete":
    print(str(myJar))
    index = int(input("Enter the index of the awesome event!\n"))
    myJar.deleteEvent(index)
  else:
    print("Unknown input! Try again!\n")



