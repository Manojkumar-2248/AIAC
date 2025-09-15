def validate_payment(card, exp, cvv):
	"""
	Validates payment card details for basic format and length requirements.

	Parameters:
		card (str): Card number as a string (should be 16 digits).
		exp (str): Expiry date in MM/YY format.
		cvv (int or str): Card Verification Value (should be 3 digits).

	Returns:
		bool: True if all details pass validation, False otherwise.

	Security & Quality Notes:
		- Does not log or print sensitive data.
		- Checks that card contains only digits and is exactly 16 characters.
		- Checks that CVV is a 3-digit number.
		- Checks that expiry date matches MM/YY format.
		- Does not perform actual payment authorization.
	"""
	# Validate card number: must be 16 digits, all numeric
	if not (isinstance(card, str) and card.isdigit() and len(card) == 16):
		return False

	# Validate CVV: must be 3 digits, all numeric
	if not (str(cvv).isdigit() and len(str(cvv)) == 3):
		return False

	# Validate expiry date: MM/YY format
	import re
	if not re.fullmatch(r"(0[1-9]|1[0-2])/\d{2}", exp):
		return False

	return True

print(validate_payment("1234567890123456", "12/25", 123))  # Sample output: True
