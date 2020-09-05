# Lesson-08 Behavior-Driven Development
### 1. Behavior-driven Development
In software engineering, behavior-driven development (BDD) is an Agile software development process that encourages collaboration among developers, QA and non-technical or business participants in a software project. It encourages teams to use conversation and concrete examples to formalize a shared understanding of how the application should behave.[4] It emerged from test-driven development (TDD). Behavior-driven development combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software development and management teams with shared tools and a shared process to collaborate on software development.

### 2. Behavioral specifications
BDD specifies that business analysts and developers should collaborate in this area and should specify behavior in terms of user stories, which are each explicitly written down in a dedicated document. Each User Story should, in some way, follow the following structure:
####Title   
An explicit title.    
####Narrative    
A short introductory section with the following structure:    
As a: the person or role who will benefit from the feature;    
I want: the feature;    
so that: the benefit or value of the feature.    
####Acceptance criteria    
A description of each specific scenario of the narrative with the following structure:  
Given: the initial context at the beginning of the scenario, in one or more clauses;  
When: the event that triggers the scenario;  
Then: the expected outcome, in one or more clauses.  

BDD does not have any formal requirements for exactly how these user stories must be written down, but it does insist that each team using BDD come up with a simple, standardized format for writing down the user stories which includes the elements listed above. However, in 2007 Dan North suggested a template for a textual format which has found wide following in different BDD software tools. A very brief example of this format might look like this:

```
Title: Returns and exchanges go to inventory.  

As a store owner,  
I want to add items back to inventory when they are returned or exchanged,  
so that I can track inventory.  

Scenario 1: Items returned for refund should be added to inventory.  
Given that a customer previously bought a black sweater from me  
and I have three black sweaters in inventory,  
when they return the black sweater for a refund,  
then I should have four black sweaters in inventory.  

Scenario 2: Exchanged items should be returned to inventory.  
Given that a customer previously bought a blue garment from me  
and I have two blue garments in inventory  
and three black garments in inventory,  
when they exchange the blue garment for a black garment,  
then I should have three blue garments in inventory  
and two black garments in inventory.  
```

### 3. Basic Example
User stories and scenarios:  
```
Title: Deposit and withdraw money

As a bank account,
I want to record money when they are deposited or withdrawed,
so that I can track balance.

Scenario 1: Money deposited should be added to balance.
Given that I have a balance of 100,
when I deposit 100,
then I should have a balance of 200.

Scenario 2: Money withdrawed should be subtracted from the balance.
Given that I have a balance of 300,
when I withdraw 200,
then I should have a balance of 100.
```
```
class Account:
    balance = 100

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

```


### 4. Exercise
Librarian should track book borrowing and returning.  
1.Write user stories and scenarios.  
2.Write methods according to user stories.