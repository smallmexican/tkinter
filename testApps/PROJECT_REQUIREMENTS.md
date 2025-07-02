# 📋 Project Requirements Document

## **Client:** TechStart Solutions
## **Project:** Personal Finance Tracker Desktop Application

---

## 🎯 **Project Overview**
Our small business needs a simple desktop application to help employees track their personal finances. The app should be intuitive, professional-looking, and help users manage their income, expenses, and savings goals.

---

## 📋 **User Stories & Requirements**

### **Epic 1: Core Financial Tracking**

#### **Story 1.1: Income Management** ✅ *In Progress*
- **As a** user
- **I want to** add and track different sources of income
- **So that** I can see my total monthly earnings
- **Acceptance Criteria:**
  - [x] Add income entries with amount, source, and date
  - [ ] View list of all income entries
  - [ ] Delete income entries
  - [ ] Show total income for current month

**Status:** Backend methods created, UI forms needed

---

#### **Story 1.2: Expense Tracking** ✅ *In Progress*
- **As a** user  
- **I want to** record and categorize my expenses
- **So that** I can understand where my money goes
- **Acceptance Criteria:**
  - [x] Add expense entries with amount, category, description, and date
  - [x] Categories include: Food, Transportation, Housing, Entertainment, Healthcare, Other
  - [ ] View list of all expenses
  - [ ] Delete expense entries

**Status:** Backend methods created, UI forms needed

---

#### **Story 1.3: Balance Overview** ✅ *Completed*
- **As a** user
- **I want to** see my current financial balance
- **So that** I know if I'm spending within my means
- **Acceptance Criteria:**
  - [x] Display current balance (Total Income - Total Expenses)
  - [x] Show balance in a prominent, easy-to-read format
  - [x] Use color coding (green for positive, red for negative)

**Status:** ✅ DONE - Dynamic labels with color coding implemented

---

### **Epic 2: Data Visualization & Reports**

#### **Story 2.1: Monthly Summary** ⏳ *Not Started*
- **As a** user
- **I want to** see a summary of my finances for the current month
- **So that** I can track my monthly financial performance
- **Acceptance Criteria:**
  - [ ] Show total income for current month
  - [ ] Show total expenses for current month  
  - [ ] Show expenses broken down by category
  - [ ] Display net savings/loss for the month

**Status:** Pending - Requires date filtering logic

---

#### **Story 2.2: Expense Categories Breakdown** ⏳ *Not Started*
- **As a** user
- **I want to** see which categories I spend the most on
- **So that** I can identify areas to cut back
- **Acceptance Criteria:**
  - [ ] Show percentage of total expenses per category
  - [ ] Display in a clear, visual format (could be text-based percentages)

**Status:** Pending - Requires category analysis logic

---

### **Epic 3: User Interface & Experience**

#### **Story 3.1: Professional Appearance** ✅ *In Progress*
- **As a** user
- **I want** the app to look professional and modern
- **So that** I feel confident using it for important financial data
- **Acceptance Criteria:**
  - [x] Clean, modern interface design
  - [x] Consistent color scheme
  - [x] Clear, readable fonts
  - [x] Proper spacing and layout

**Status:** Basic layout created, needs navigation and forms

---

#### **Story 3.2: Easy Navigation** ⏳ *Not Started*
- **As a** user
- **I want** to easily switch between different views/functions
- **So that** I can efficiently manage my financial data
- **Acceptance Criteria:**
  - [ ] Clear navigation between Income, Expenses, and Summary views
  - [ ] Intuitive button placement and labeling
  - [ ] Keyboard shortcuts for common actions

**Status:** Pending - Need to design navigation system

---

### **Epic 4: Data Management**

#### **Story 4.1: Data Validation** ⚠️ *Partially Complete*
- **As a** user
- **I want** the app to prevent invalid data entry
- **So that** my financial records remain accurate
- **Acceptance Criteria:**
  - [x] Only allow positive numbers for amounts
  - [ ] Require all mandatory fields before saving
  - [ ] Show clear error messages for invalid input
  - [ ] Default to current date for new entries

**Status:** Basic validation in backend, UI validation needed

---

#### **Story 4.2: Edit Functionality** ⏳ *Not Started*
- **As a** user
- **I want** to edit existing income and expense entries
- **So that** I can correct mistakes or update information
- **Acceptance Criteria:**
  - [ ] Double-click or button to edit existing entries
  - [ ] Save changes to existing entries
  - [ ] Cancel edit operation

**Status:** Not started - requires data structure changes

---

## 🎨 **Design Requirements**

### **Window Specifications:**
- [x] Main window: 800x600 pixels minimum
- [x] Application title: "Personal Finance Tracker"  
- [x] Should be resizable: Currently set to non-resizable

### **UI Components Needed:**
- [ ] Tab-based navigation OR button-based navigation
- [ ] Data entry forms
- [ ] List displays for income/expenses
- [x] Summary dashboard area
- [ ] Add/Edit/Delete buttons

### **Visual Requirements:**
- [x] Use consistent color scheme throughout
- [x] Green for positive amounts/income
- [x] Red for negative amounts/expenses
- [x] Professional fonts (Arial, Segoe UI, or similar)
- [x] Proper padding and margins

---

## 🔧 **Technical Constraints**

- [x] Must use Python with tkinter
- [x] Should work on Windows (primary target)
- [x] No external database required (can store in memory for now)
- [x] Should handle basic input validation
- [x] Must be a single executable Python file

---

## 📝 **Current Technical Issues to Fix**

### **Data Structure Problems:**
1. **❌ Expenses Storage Bug:**
   ```python
   # Current (WRONG):
   self.expensises["description"] = amount  # This overwrites data!
   
   # Should be (FIX NEEDED):
   self.expenses.append({
       "description": description,
       "amount": amount,
       "category": category,
       "date": datetime.now()
   })
   ```

2. **❌ Income Storage Bug:**
   ```python
   # Same issue with income storage - needs to be a list, not dict
   ```

3. **❌ Typo:** `self.expensises` should be `self.expenses`

---

## 🚀 **Next Development Steps**

### **Immediate Priority (MVP):**
1. **Fix data storage structure** - Use lists instead of single dictionaries
2. **Create input forms** - Add UI for entering income/expenses
3. **Create data display** - Show lists of transactions
4. **Add navigation** - Tab or button-based switching between views

### **Suggested Implementation Order:**
1. ✅ ~~Fix data structures~~
2. 🔄 Create "Add Income" form
3. 🔄 Create "Add Expense" form  
4. 🔄 Create transaction history view
5. 🔄 Add edit/delete functionality
6. 🔄 Create monthly summary view
7. 🔄 Add category breakdown
8. 🔄 Polish UI and validation

---

## 📝 **Optional Enhancements** (if time permits)

- [ ] Save/Load data to file
- [ ] Date range filtering
- [ ] Simple charts or graphs
- [ ] Export data to text file
- [ ] Calculator widget for quick calculations

---

## 🎯 **Current Status Summary**

**✅ Completed:**
- Basic window setup and layout
- Dynamic balance display with color coding
- Backend calculation methods (with bugs to fix)

**🔄 In Progress:**
- Data entry functionality
- Professional UI design

**⏳ Not Started:**
- Navigation system
- Transaction history display
- Monthly reports
- Data persistence

---

**📅 Last Updated:** June 30, 2025
**🔥 Priority:** Fix data storage bugs, then create input forms

---

## 💡 **Development Notes**

- Focus on getting basic CRUD (Create, Read, Update, Delete) working first
- Keep the UI simple and clean - function over form initially
- Test each feature thoroughly before moving to the next
- Consider using `ttk` widgets for more modern appearance
- Remember to validate all user inputs

---

*Good luck with your development! Remember to start simple and build incrementally. Focus on getting the core functionality working before adding advanced features.* 🎯
