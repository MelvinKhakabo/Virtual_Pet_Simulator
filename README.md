# Virtual_Pet_Simulator
Virtual Pet Simulator Python Project

##  Project Idea: Virtual Pet Simulator
### Objective
Create a Python program where users can take care of a virtual pet, ensuring it remains happy, healthy, and fed. The pet's needs will change over time, requiring attention.

### Features
#### Create Your Pet
Allow users to name and choose the type of their pet (e.g., dog, cat, bird).
#### Pet Stats
Track the pet's health, happiness, hunger, and energy levels.
#### Interact with Your Pet
Feed, play with, or let the pet rest to improve its stats.
#### Dynamic Changes
Gradually decrease stats over time if the pet isn’t cared for, leading to consequences like sickness or running away.
#### Save & Load Progress
Persist the pet's state between sessions.


### How It Works:
#### Creating a Pet:
Users name their pet and specify its type. Initial stats are set (e.g., hunger, happiness).

#### Managing Stats:
Hunger, happiness, health, and energy decrease over time.
Users can interact with the pet to restore its stats.

#### Interactions:
Feed: Increases hunger and slightly improves health.
Play: Increases happiness but reduces energy.
Rest: Increases energy.

#### Dynamic Events:
Neglecting the pet reduces health and can lead to its "death."

#### Save & Load:
Pet progress is saved in a JSON file and reloaded on the next session.