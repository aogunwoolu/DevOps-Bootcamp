## Scrum part 2

**if there is a problematic member**: the scrum master should take charge dealing with it

**stakeholders** (people who have an interest in the project) pick themselves,

	- stakeholders power refers to the influence of said stakeholder

In agile environment, ___pull___ don't push:

- don't send unsolicited progress reports
- stakeholders pull information from team (respond to requests/requirements)

scrum guide states ___the Product Owner is responsible for maximising the value of the product and the work of the Development Team___ 

- product owner defines the value
- development team delivers the value across successive sprints

___considerations for value___:

1. **entry conditions** - deliver minimum required feature set (MMF) - achieve compliancy
2. **enablement** - targeting new markets - enable sales of other products & services
3. **differentiator** - differentiate from competitors - delight customers
4. **spoiler** - eliminate competitors' differentiator - redefine the game by changing market focus
5. **cost reducer** - shorten time to market - increase expertise

user stories:

- Perspective/context
- functional requirement
- Goal/outcome
- **used as a basis for a conversation**

user story test:

**I**ndependent 

- of order of user story delivery
- of internal and ___especially___ external dependences

**N**egotiable

- flexible scope
- none specific language
- explain the intention, __not the implementation__

**V**aluable

- value is clear to everyone
- Persona matches benefit & goal will deliver the benefit
- avoid technical/role language

**E**stimatable:

- clear & consise explaination
- avoid technical/role specific language

**S**mall:

- easily fits into a sprint i.e. <20% of velocity
- ___dont___ >33% of velocity

**T**estable:

- can be automated
- Avoid external testing/long test suites 

## Product backlog items (PBI)

- Task/work. needed to be complete

- forms PBIs can take:

  - user stories
  - use cases
  - technical debt/bugs/defects
  - constraints
    - Limitations: something that can't be changed
    - public holidays
  - refactoring
    - changing the structure and implementation of code
  - spike
    - experiemnt and learn
  - enablers
    - technical
    - allowing DNZ to accept packets via setting ports

  **D**.**E**.**E**.**P**:

  - **D**etail appropriately

    - only detail higher priority tickets

  - **E**stimated

  - **E**mergent

  - **P**rioritised

    - **stacked prioritisation**:

      - most important at the top

    - **MOSCOW prioritisation**

      - ___M___ust _have this time_
        - vital, without it: there is no value
        - <strong>60% of the effort</strong>
      - ___S___hould _have this time_
        - Important, but not vital
        - <strong>20% of the effort</strong>
      - ___C___ould _have this time_
        - if the time allows, get it done
        - <strong>20% of the effort</strong>
      - ___W___on't _have this time_
        - out of scope
      - can only be used in a sprint/project (something that has a timeframe)
      - always do **must** have first

    - **Weighted Shortest Job First**

      - $$
        Priority = \frac{cost of delay}{job size}
        $$

        

  ## estimation

  a prediciton based on the constraints that are set

  - reducing/highlighting risk
  - reducing uncertainty
  - support better decision making
  - establishing trust
  - conveying information 

**Boehm's cone of uncertainty**:

![CeyEbXE](https://i.imgur.com/CeyEbXE.png)

to reduce extended time frame estimation due to miscommunication, involve the whole team

**relative estimation techniques**:

- ***T-shirt***: **S**mall, **M**edium **L**arge
- ***Delphi***: Assign points independently then discuss and assign again and again
- ***Scale***: 0, 1, 2, 3, 5, 8, 13, 21
  - 0 scale is put on features already implemented 
  - gaps getting bigger because of the larger uncertainty
- ***poke cards***: each member has set of cards with points and declares their hand
  - waiting for everyone to draw a card about the uncertainty 
  - numbered cards
- ***RPS***: **R**ock, **P**aper, **S**cissors
  - showing how big the job is with fingers
