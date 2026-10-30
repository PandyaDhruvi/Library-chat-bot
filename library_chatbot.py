"""
Library Chatbot - Rule-Based System
Topic: Library
Method: Python if-else conditions
Students: Group of 2
Assignment: GMIU Web Portal
"""

def library_chatbot(user_input):
    """
    A rule-based chatbot for a Library system.
    Returns appropriate responses based on user input using if-else conditions.
    """
    # Normalize input: lowercase and strip whitespace
    user_input = user_input.lower().strip()

    # -------------------------------------------------------
    # 1. GREETINGS
    # -------------------------------------------------------
    if user_input in ["hi", "hello", "hey", "good morning", "good evening", "greetings", "namaste"]:
        return (
            "👋 Welcome to the City Library Chatbot!\n"
            "I can help you with:\n"
            "  📚 Book Search & Availability\n"
            "  🕒 Library Hours\n"
            "  🪪 Membership & Registration\n"
            "  🔁 Book Renewal\n"
            "  💰 Fines & Late Fees\n"
            "  📖 Reading Room\n"
            "  🌐 Digital Resources\n"
            "  📞 Contact Information\n\n"
            "How can I assist you today?"
        )

    # -------------------------------------------------------
    # 2. FAREWELLS
    # -------------------------------------------------------
    elif user_input in ["bye", "goodbye", "exit", "quit", "see you", "thank you", "thanks"]:
        return "📚 Thank you for visiting City Library Chatbot. Have a wonderful day! Goodbye! 👋"

    # -------------------------------------------------------
    # 3. LIBRARY HOURS
    # -------------------------------------------------------
    elif any(word in user_input for word in ["hour", "timing", "time", "open", "close", "schedule", "when"]):
        return (
            "🕒 Library Working Hours:\n"
            "  Monday - Friday  : 9:00 AM – 8:00 PM\n"
            "  Saturday          : 10:00 AM – 6:00 PM\n"
            "  Sunday            : 11:00 AM – 4:00 PM\n"
            "  Public Holidays   : Closed\n\n"
            "Note: Reading Room is open 24/7 for registered members."
        )

    # -------------------------------------------------------
    # 4. BOOK SEARCH / AVAILABILITY
    # -------------------------------------------------------
    elif any(word in user_input for word in ["book", "search", "find", "available", "availability", "novel", "title", "author"]):
        return (
            "📚 Book Search & Availability:\n"
            "  1. Visit our online catalogue at: www.citylibrary.in/catalogue\n"
            "  2. Use the search bar on the library counter terminal.\n"
            "  3. Ask the librarian at the Help Desk (Counter No. 1).\n\n"
            "Search by:\n"
            "  🔹 Title   🔹 Author   🔹 ISBN   🔹 Subject\n\n"
            "If a book is currently issued, you can place a HOLD/RESERVATION.\n"
            "Type 'reservation' for more info."
        )

    # -------------------------------------------------------
    # 5. MEMBERSHIP / REGISTRATION
    # -------------------------------------------------------
    elif any(word in user_input for word in ["member", "membership", "register", "registration", "join", "card", "library card", "enroll"]):
        return (
            "🪪 Library Membership:\n\n"
            "  Types of Membership:\n"
            "  ─────────────────────────────────────\n"
            "  🟢 Student     : ₹200/year  (5 books)\n"
            "  🔵 General     : ₹500/year  (7 books)\n"
            "  🟣 Senior Citizen: ₹100/year (7 books)\n"
            "  ─────────────────────────────────────\n\n"
            "  Documents Required:\n"
            "  • ID Proof (Aadhar / College ID)\n"
            "  • Passport-size photograph (2 copies)\n"
            "  • Address Proof\n\n"
            "  Visit Counter No. 2 to register.\n"
            "  Processing time: Same day ✅"
        )

    # -------------------------------------------------------
    # 6. BOOK ISSUE
    # -------------------------------------------------------
    elif any(word in user_input for word in ["issue", "borrow", "take", "checkout", "check out", "lend"]):
        return (
            "📤 Issuing a Book:\n\n"
            "  Steps to Borrow a Book:\n"
            "  1. Search for the book in the catalogue.\n"
            "  2. Note the Accession Number / Call Number.\n"
            "  3. Go to the Book Issue Counter (Counter No. 3).\n"
            "  4. Show your Library Card.\n"
            "  5. Book will be issued for 14 days.\n\n"
            "  Limits:\n"
            "  • Student: 5 books at a time\n"
            "  • General: 7 books at a time\n\n"
            "  ⚠️ Late fine: ₹2 per day per book after due date."
        )

    # -------------------------------------------------------
    # 7. BOOK RETURN
    # -------------------------------------------------------
    elif any(word in user_input for word in ["return", "submit", "give back"]):
        return (
            "📥 Returning a Book:\n\n"
            "  Steps to Return:\n"
            "  1. Visit the Book Return Counter (Counter No. 3).\n"
            "  2. Hand over the book to the librarian.\n"
            "  3. Collect your return receipt.\n\n"
            "  ⏰ Return books within 14 days to avoid fines.\n"
            "  💡 Tip: You can also use the self-return drop box near the main entrance."
        )

    # -------------------------------------------------------
    # 8. BOOK RENEWAL
    # -------------------------------------------------------
    elif any(word in user_input for word in ["renew", "renewal", "extend", "extension"]):
        return (
            "🔁 Book Renewal:\n\n"
            "  Options to Renew:\n"
            "  1. 🌐 Online  : www.citylibrary.in/renew (Login required)\n"
            "  2. 📞 Phone   : Call 1800-LIB-RENEW (Mon–Sat)\n"
            "  3. 🏛️ In-Person: Visit Counter No. 3\n\n"
            "  Rules:\n"
            "  • Maximum 2 renewals per book\n"
            "  • Renewal not allowed if book is reserved by another member\n"
            "  • Renewal must be done before due date\n"
            "  • Each renewal extends loan period by 7 days"
        )

    # -------------------------------------------------------
    # 9. FINES / LATE FEES
    # -------------------------------------------------------
    elif any(word in user_input for word in ["fine", "penalty", "late", "overdue", "fee", "charge"]):
        return (
            "💰 Fine & Penalty Policy:\n\n"
            "  📌 Late Return Fine:\n"
            "  • ₹2 per book per day after due date\n\n"
            "  📌 Lost Book Fine:\n"
            "  • Pay the current price of the book + ₹100 processing fee\n\n"
            "  📌 Damaged Book Fine:\n"
            "  • Minor damage : ₹50\n"
            "  • Major damage : Full book price\n\n"
            "  📌 Payment Methods:\n"
            "  • Cash at Counter No. 4\n"
            "  • Online via library portal\n"
            "  • UPI / QR Code at counter\n\n"
            "  ⚠️ Unpaid fines will block your library account."
        )

    # -------------------------------------------------------
    # 10. BOOK RESERVATION / HOLD
    # -------------------------------------------------------
    elif any(word in user_input for word in ["reserv", "hold", "request", "waiting", "waitlist", "pre-book"]):
        return (
            "📋 Book Reservation / Hold:\n\n"
            "  How to Reserve a Book:\n"
            "  1. Check if book is currently issued (not available).\n"
            "  2. Login to www.citylibrary.in/catalogue\n"
            "  3. Click 'Place Hold' on the book page.\n"
            "  4. You will get an SMS/Email when book is available.\n\n"
            "  Hold Period:\n"
            "  • Book is kept on hold for 2 days after availability notice.\n"
            "  • If not collected, hold is cancelled automatically.\n\n"
            "  Max holds: 3 books at a time."
        )

    # -------------------------------------------------------
    # 11. READING ROOM
    # -------------------------------------------------------
    elif any(word in user_input for word in ["reading room", "study", "study room", "reading", "silent zone", "reading area"]):
        return (
            "📖 Reading Room:\n\n"
            "  🏛️ Reading Room A (General)\n"
            "  • Open: 9:00 AM – 8:00 PM (All days)\n"
            "  • Capacity: 80 seats\n"
            "  • Free entry with Library Card\n\n"
            "  🌙 Reading Room B (24/7 for Members)\n"
            "  • Open: 24 Hours, 7 Days\n"
            "  • Capacity: 40 seats\n"
            "  • Requires: Active membership\n"
            "  • Facilities: WiFi, AC, Power sockets\n\n"
            "  📵 Rules: No mobile usage | Maintain silence | No food/drinks"
        )

    # -------------------------------------------------------
    # 12. DIGITAL RESOURCES / E-LIBRARY
    # -------------------------------------------------------
    elif any(word in user_input for word in ["digital", "ebook", "e-book", "online", "internet", "wifi", "e-resource", "electronic", "pdf", "journal"]):
        return (
            "🌐 Digital Resources & E-Library:\n\n"
            "  Access through: www.citylibrary.in/digital\n\n"
            "  Available Resources:\n"
            "  📘 eBooks         - 10,000+ titles\n"
            "  📰 e-Journals     - 500+ journals\n"
            "  🎓 NPTEL Lectures - Free access\n"
            "  📄 Research Papers- via Shodhganga\n"
            "  📚 DELNET         - Inter-library loans\n\n"
            "  🔑 Login: Use your Library Member ID\n"
            "  📶 Free WiFi available inside the library\n"
            "  Tip: You can access eBooks from home using your credentials!"
        )

    # -------------------------------------------------------
    # 13. CONTACT INFORMATION
    # -------------------------------------------------------
    elif any(word in user_input for word in ["contact", "phone", "call", "email", "address", "location", "where", "help desk"]):
        return (
            "📞 Contact Us:\n\n"
            "  🏛️  City Library\n"
            "  📍  123, Knowledge Park, Main Road, City - 380001\n\n"
            "  📞  Landline : 079-2234-5678\n"
            "  📱  Mobile   : +91-98765-43210\n"
            "  📧  Email    : info@citylibrary.in\n"
            "  🌐  Website  : www.citylibrary.in\n\n"
            "  Help Desk: Counter No. 1 (Inside main entrance)\n"
            "  Librarian: Mr. Ramesh Patel (Head Librarian)\n\n"
            "  🕒 Call us during working hours (9 AM – 8 PM, Mon–Sat)"
        )

    # -------------------------------------------------------
    # 14. SERVICES
    # -------------------------------------------------------
    elif any(word in user_input for word in ["service", "facility", "facilities", "what do you offer", "what can", "offer"]):
        return (
            "🏛️ Library Services:\n\n"
            "  📚 Book Lending       - Issue & Return books\n"
            "  📋 Reservation        - Hold books in advance\n"
            "  🔁 Renewal            - Extend loan period\n"
            "  📖 Reading Rooms      - Silent study spaces\n"
            "  🌐 Digital Library    - eBooks, Journals, Research\n"
            "  📶 Free WiFi          - Throughout library\n"
            "  🖨️  Photocopy/Print   - ₹1 per page (B&W)\n"
            "  🎓 Competitive Exams  - Special book collection\n"
            "  👨‍🏫 Librarian Help    - Guidance & Reference help\n"
            "  🔐 Locker Facility    - ₹50/month\n\n"
            "  Type any service name for more details!"
        )

    # -------------------------------------------------------
    # 15. LOCKER FACILITY
    # -------------------------------------------------------
    elif any(word in user_input for word in ["locker", "bag", "storage", "luggage"]):
        return (
            "🔐 Locker / Bag Storage:\n\n"
            "  • Lockers available near the main entrance\n"
            "  • Charges: ₹50/month or ₹5/day\n"
            "  • Key deposit: ₹100 (refundable)\n"
            "  • Personal bags NOT allowed inside reading rooms\n"
            "  • Inquire at Counter No. 1\n\n"
            "  📦 Day storage is free for 3 hours with Library Card."
        )

    # -------------------------------------------------------
    # 16. PHOTOCOPY / PRINT
    # -------------------------------------------------------
    elif any(word in user_input for word in ["photocopy", "print", "copy", "xerox", "scan"]):
        return (
            "🖨️ Photocopy & Printing Services:\n\n"
            "  📍 Location: Ground Floor, Near Exit\n\n"
            "  Charges:\n"
            "  • Black & White Print/Copy : ₹1 per page\n"
            "  • Colour Print             : ₹5 per page\n"
            "  • Scanning                 : ₹2 per page\n"
            "  • A4 / A3 size available\n\n"
            "  ⏰ Available: 9 AM – 7 PM (Mon–Sat)\n"
            "  💳 Payment: Cash or UPI"
        )

    # -------------------------------------------------------
    # 17. COMPETITIVE EXAM / REFERENCE SECTION
    # -------------------------------------------------------
    elif any(word in user_input for word in ["exam", "competitive", "upsc", "gpsc", "ssc", "gate", "reference", "dictionary", "encyclopaedia"]):
        return (
            "🎓 Competitive Exam & Reference Section:\n\n"
            "  📚 Special collection for:\n"
            "  • UPSC / GPSC / SSC / NEET / JEE\n"
            "  • GATE / GRE / GMAT / CAT\n"
            "  • Government Job Exams\n\n"
            "  📍 Location: First Floor, Section C\n\n"
            "  ⚠️ Reference books CANNOT be issued (in-house reading only)\n"
            "  📖 Encyclopaedias, Dictionaries, Yearbooks available\n"
            "  🕒 Open: 9 AM – 8 PM (All days)"
        )

    # -------------------------------------------------------
    # 18. LOST CARD
    # -------------------------------------------------------
    elif any(word in user_input for word in ["lost card", "lost my card", "duplicate card", "replace card", "missing card"]):
        return (
            "🪪 Lost Library Card:\n\n"
            "  If you lost your Library Card:\n"
            "  1. Report immediately at Counter No. 2\n"
            "  2. Fill the 'Lost Card' form\n"
            "  3. Pay duplicate card fee: ₹50\n"
            "  4. New card issued within 30 minutes\n\n"
            "  📞 You can also report by calling: 079-2234-5678\n"
            "  ⚠️ You are responsible for any misuse until you report the loss."
        )

    # -------------------------------------------------------
    # 19. DONATION / NEW BOOKS
    # -------------------------------------------------------
    elif any(word in user_input for word in ["donat", "new book", "new arrival", "suggest book", "add book", "recently added"]):
        return (
            "📬 New Books & Donations:\n\n"
            "  🆕 New Arrivals:\n"
            "  • Check our website: www.citylibrary.in/new-arrivals\n"
            "  • New books list displayed at main noticeboard\n"
            "  • Updated every Monday\n\n"
            "  📤 Book Donations:\n"
            "  • We accept donations of books in good condition\n"
            "  • Visit Counter No. 2 with the books\n"
            "  • Receive a donation certificate\n\n"
            "  💡 Suggest a Book:\n"
            "  • Fill the 'Book Suggestion' form at Counter No. 1\n"
            "  • Or email: suggest@citylibrary.in"
        )

    # -------------------------------------------------------
    # 20. DEFAULT / UNKNOWN INPUT
    # -------------------------------------------------------
    else:
        return (
            "🤔 Sorry, I didn't understand that.\n\n"
            "You can ask me about:\n"
            "  • 'Library hours'       - Timings\n"
            "  • 'Book search'         - Find books\n"
            "  • 'Membership'          - Join library\n"
            "  • 'Issue a book'        - Borrow books\n"
            "  • 'Return a book'       - Return process\n"
            "  • 'Renew a book'        - Extend due date\n"
            "  • 'Fines'               - Late fee info\n"
            "  • 'Reading room'        - Study spaces\n"
            "  • 'Digital resources'   - eBooks & journals\n"
            "  • 'Services'            - All services\n"
            "  • 'Contact'             - Library contact info\n\n"
            "Type 'bye' to exit. How can I help you? 😊"
        )


def main():
    """Main function to run the chatbot in terminal."""
    print("=" * 60)
    print("         📚 CITY LIBRARY CHATBOT 📚")
    print("         Rule-Based Chatbot | Python")
    print("         Topic: Library Services")
    print("=" * 60)
    print("Type 'bye' or 'exit' to quit the chatbot.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Bot: Please enter a message.\n")
            continue

        response = library_chatbot(user_input)
        print(f"\nBot: {response}\n")
        print("-" * 60)

        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
