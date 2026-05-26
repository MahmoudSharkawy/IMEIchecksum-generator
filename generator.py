import sys

class ChecksumGenerator:
    """High-performance 15-digit checksum generator and validator."""
    
    @staticmethod
    def generate(payload: int) -> int:
        """
        Generates a 1-digit checksum for a 14-digit integer payload,
        resulting in a complete 15-digit validated ID.
        """
        if not (10**13 <= payload < 10**14):
            raise ValueError("Payload must be exactly 14 digits long.")
        
        total_sum = 0
        temp = payload
        
        # Process digits from right to left (14 digits total)
        for i in range(14):
            digit = temp % 10
            temp //= 10
            
            # Alternate doubling based on position (Luhn variant)
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            
            total_sum += digit
            
        # Calculate the check digit
        check_digit = (10 - (total_sum % 10)) % 10
        return (payload * 10) + check_digit

    @staticmethod
    def validate(full_code: int) -> bool:
        """Validates a complete 15-digit checksum integer."""
        if not (10**14 <= full_code < 10**15):
            return False
            
        payload = full_code // 10
        provided_checksum = full_code % 10
        
        try:
            expected_code = ChecksumGenerator.generate(payload)
            return expected_code == full_code
        except ValueError:
            return False

# --- Interactive CLI Wrapper ---
if __name__ == "__main__":
    print("=" * 45)
    print("   🚀 15-Digit Checksum Generator App   ")
    print("=" * 45)
    print("1. Generate 15-Digit Code (Input 14 digits)")
    print("2. Validate 15-Digit Code")
    print("3. Exit")
    print("-" * 45)
    
    while True:
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            try:
                user_in = int(input("Enter a 14-digit base payload: "))
                result = ChecksumGenerator.generate(user_in)
                print(print(f"✅ Generated 15-Digit ID: {result}"))
            except ValueError as e:
                print(f"❌ Error: {e}. Please enter exactly 14 numerical digits.")
                
        elif choice == '2':
            try:
                user_in = int(input("Enter 15-digit code to validate: "))
                is_valid = ChecksumGenerator.validate(user_in)
                if is_valid:
                    print("✅ Status: VALID Checksum.")
                else:
                    print("❌ Status: INVALID Checksum.")
            except ValueError:
                print("❌ Error: Please enter a valid number.")
                
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")