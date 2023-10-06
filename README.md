The provided Python code represents a functional Automated Teller Machine (ATM) system based on a detailed description. This ATM system, accessible through a text-based interface, offers a range of services to users, maintaining security, and providing essential banking functionalities.
**Main Menu:**
  The system greets users with a clear main menu, offering three primary options: Create Account, Checkin, and Exit.
**Create Account:**
  Upon selecting this option, the system guides the user through the account creation process. It collects the user's name, initial deposit (which must exceed 50 currency units), and a 4-digit PIN code. The system then auto-generates a unique 10-digit ID, and a username (a combination of the user's name and a random number), and sets the user's status to "ACTIVE." Currency is standardized to PKR (Pakistani Rupee). An initial deposit transaction is added to the user's transaction statement. User data is saved in a users.txt file as a dictionary.
**Checkin:**
  Users can log in to their accounts by providing either their account number or username. If the entered credentials are incorrect three times, the user's status is updated to "BLOCKED" for security purposes. Once logged in, users access a sub-menu with options to view their account details, deposit funds, withdraw, update their PIN, check their transaction statement, or log out.
**Account Detail:**
  This option displays the user's personal information, including their name, username, status, and current balance in PKR.
**Deposit:**
  Users can add funds to their accounts. They enter the deposit amount, which must exceed 50 PKR, and the system updates their balance and transaction statement accordingly.
**Withdraw:**
  This feature enables users to withdraw funds from their accounts. A 1% tax is applied to the withdrawal amount. The system verifies if the withdrawal amount (plus tax) is within the user's balance. If so, the transaction is completed, and the user's balance is updated. Blocked users cannot withdraw unless their status is set back to "ACTIVE."
**Update PIN:**
  Users can change their PINs for added security. The system requests the previous PIN for verification and, if correct, allows the user to set a new 4-digit PIN.
**Check Statement:**
  Users can view their transaction history. The system generates a username_statement.txt file containing each entry from the user's statement, with each transaction on a separate line.
**Logout:**
  This option allows users to securely log out of their accounts, returning them to the main menu.
**Exit:**
  Users can exit the program at any time.
