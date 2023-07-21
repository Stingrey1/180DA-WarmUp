#include <string>
#include "CricketTeam.h"



// constructor
CricketTeam::CricketTeam(){

	// initializes an empty set
	
	head = nullptr;
	tail = nullptr;
	m_size = 0;
	
}

// destructor
CricketTeam::~CricketTeam() {

	if (!(noTeam()))
	{
		Node* current = head;
		while (current != nullptr)
		{
			Node* next = current->nextNode;
			delete current;
			current = next;
		}
	}

	head = nullptr;
	tail = nullptr;
	m_size = 0;

}

// copy constructor

CricketTeam::CricketTeam(const CricketTeam& other)
{
	// empty
	if (other.head == nullptr)
	{
		head = nullptr;
		tail = nullptr;
		m_size = 0;
		return;
	}

	this->head = nullptr;
	this->tail = nullptr;
	this->m_size = 0;

	// copy values over
	/*int size = other.m_size();
	for (int i = 0; i < size; i++)
	{
		ItemType x;
		other.get(i, x);
		insert(i, x);
	}*/
}
// assignment operator
CricketTeam& CricketTeam::operator=(const CricketTeam& rhs) 
{
	// checks for aliasing
	if (this != &rhs) {
		CricketTeam temp(rhs); // creates temporary copy of rhs
		tradeCricketTeams(temp); // switches contents of lhs and temp using the swap (tradeCricketTeam function)
	} 
	
	// temp should be destroyed at the end of this loop and the dynamically allocated memory will be cleared 

	return *this;
}


bool CricketTeam::noTeam() const
{

	return (m_size == 0); // if no items in list, then returns true (noTeam)
}


int CricketTeam::cricketerCount() const
{
	return m_size; // since we have a counter of the number of items in our LL, we can just return the number in the LL
}

bool CricketTeam::addCricketer(const std::string& firstName, const std::string&
	lastName, const CricketType& value)
{

	// iterate through the list to see if there's a match
	// if there's match, then return false
	// else return true

	if (m_size == 0)  // if we have an empty list, then we could just make new list and add to front
	{
		Node* newNode = new Node;
		newNode->m_item = value;
		newNode->prevNode = nullptr;
		newNode->nextNode = nullptr;

		newNode->nameF = firstName;
		newNode->nameL = lastName;

		// sets head and tail
		head = newNode;
		tail = newNode;

		//increment size 
		m_size++;
		return true;
	}

	// if name same then return false
	else if (rosteredOnCricketTeam(firstName, lastName) == true)
		return false;

	// name not same so add
	else
		for (Node* curr = head; curr != nullptr; curr = curr->nextNode)
		{
			// now we need to see where to add the new node

			//continue to go if last name not between two nodes
			if ((curr->nameL < lastName) && (curr->nextNode->nameL < lastName))
				continue;

			// add at beginning
			else if (curr->nameL > lastName)
			{
				Node* newNode = new Node;
				newNode->m_item = value;

				newNode->prevNode = nullptr;
				newNode->nextNode = curr;

				newNode->nameF = firstName;
				newNode->nameL = lastName;

				// sets prev and next
				curr->prevNode = newNode;
			
				// set head
				head = newNode;

				//increment size 
				m_size++;
				return true;
			}

			// add at end of list
			else if((curr->nameL < lastName) && (curr->nextNode== nullptr)))
			{
				Node* newNode = new Node;
				newNode->m_item = value;

				newNode->prevNode = curr;
				newNode->nextNode = nullptr;

				newNode->nameF = firstName;
				newNode->nameL = lastName;

				// sets prev and next
				curr->nextNode = newNode;
			
				// set tail

				tail = newNode;
				//increment size 
				m_size++;
				return true;
			}

			// last name diff, insert here
			// will take care of end of list case, so ignore setting head and tail
			else if ((curr->nameL < lastName)  && (curr->nextNode->nameL > lastName))
			{
				// TODO
				Node* newNode = new Node;
				newNode->m_item = value;

				newNode->prevNode = curr;
				newNode->nextNode = curr->nextNode;

				newNode->nameF = firstName;
				newNode->nameL = lastName;

				// sets prev and next
				curr->nextNode->prevNode = newNode;
				curr->nextNode = newNode;
			

				//increment size 
				m_size++;
				return true;
			}


			// last case is if there are multiple same last names
			else if (curr->nameL == lastName)  
			{
				//TODO
				//first name in front
				if ((curr->nameF > firstName) && (curr->prevNode == nullptr)) 
				{
					Node* newNode = new Node;
					newNode->m_item = value;

					newNode->prevNode = nullptr;
					newNode->nextNode = curr;

					newNode->nameF = firstName;
					newNode->nameL = lastName;

				// sets prev and next
				
				curr->prevNode = newNode;
			
				//set head
				head = newNode;

				//increment size 
				m_size++;
				return true;
				}

				// add in front of curr but not at the front of the list
				else if (curr->nameF > firstName)
				{
					Node* newNode = new Node;
					newNode->m_item = value;

					newNode->prevNode = nullptr;
					newNode->nextNode = curr;

					newNode->nameF = firstName;
					newNode->nameL = lastName;

				// sets prev and next
				
				curr->prevNode = newNode;
			
				//set head
				head = newNode;

				//increment size 
				m_size++;
				return true;
				}


				// if between two first names
				else if ((curr->nameF < firstName) &&(curr->nextNode->nameF > firstName))
				{
					Node* newNode = new Node;
					newNode->m_item = value;

					newNode->prevNode = curr;
					newNode->nextNode = curr->nextNode;

					newNode->nameF = firstName;
					newNode->nameL = lastName;

				// sets prev and next
				
				curr->nextNode = newNode;
				newNode->nextNode->prevNode = newNode;
			
				

				//increment size 
				m_size++;
				return true;
				}


				else
					continue;


				
			}
		

		}

		return true;
}


bool CricketTeam::substituteCricketer(const std::string& firstName, const std::string& lastName, const CricketType& value)
{
	for (Node* curr = head; curr != nullptr; curr = curr->nextNode)  // we could also us (for int i = 0; i< size; i++)
	{ 
		if ((curr->nameF == firstName)  && (curr->nameL == lastName))


		return true; 
		// returns true if value is found
	}

	return false;
}

bool CricketTeam::addOrSubstitute(const std::string& firstName, const std::string& lastName, const CricketType& value)
{
	return true; // dummy value, always return true
}

bool CricketTeam::releaseCricketer(const std::string& firstName, const std::string& lastName)
{
	//if there a match, remove and return true, else return false

	for (Node* curr = head; curr != nullptr; curr = curr->nextNode)  // we could also us (for int i = 0; i< size; i++)
	{ 
		if ((curr->nameF == firstName)  && (curr->nameL == lastName))
		{

				// update head and tail
			if (curr->nextNode == nullptr)
				tail = curr->prevNode;
			if (curr->prevNode == nullptr)
				head = curr->nextNode;

			curr->prevNode->nextNode = curr->nextNode;
			curr->nextNode->prevNode = curr->prevNode;


		
			delete curr;

			return true; 
			// returns true if value is found
		}
		
	}

	return false;
}

// parts of the code for this part can be reused everywhere to check if name is on roster
bool CricketTeam::rosteredOnCricketTeam(const std::string& firstName, const std::string& lastName) const
{
	
	// iterates through linked list
	for (Node* curr = head; curr != nullptr; curr = curr->nextNode)  // we could also us (for int i = 0; i< size; i++)
	{ 
		if ((curr->nameF == firstName)  && (curr->nameL == lastName))
			return true; 
		// returns true if value is found
	}

	return false;
}


bool CricketTeam::searchForCricketer(const std::string& firstName, const std::string& lastName, CricketType& value) const
{
	return true; // dummy value
}

bool CricketTeam::checkTeamForCricketer(int i, std::string& firstName, std::string& lastName, CricketType& value) const
{
	if (i>= 0 && i<m_size)
		return true;

	else 
		return false; // dummy value
}

void CricketTeam::tradeCricketTeams(CricketTeam& other)
{
	//swap head
	Node* tempH = head;
	head = other.head;
	other.head = tempH;

	//swap tail
	Node* tempT = tail;
	tail = other.tail;
	other.tail = tempT;

	//swap size
	int tempSize = m_size;
	m_size = other.m_size;
	other.m_size = tempSize;;
}


