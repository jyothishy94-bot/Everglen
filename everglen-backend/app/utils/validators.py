"""
Data validation utilities
"""

import re
from typing import Optional


class IdentityValidator:
    """Validators for Indian identity documents"""

    @staticmethod
    def validate_fssai(fssai_number: str) -> bool:
        """Validate 14-digit FSSAI registration number"""
        pattern = r'^\d{14}$'
        return bool(re.match(pattern, fssai_number))

    @staticmethod
    def validate_pan(pan_number: str) -> bool:
        """Validate PAN card format (10 characters)"""
        pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
        return bool(re.match(pattern, pan_number))

    @staticmethod
    def validate_gstin(gstin: str) -> bool:
        """Validate GSTIN format (15 characters)"""
        pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{3}$'
        return bool(re.match(pattern, gstin))

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Validate Indian phone number format"""
        # Accept +91 or 91 or just 10 digits
        pattern = r'^(\+?91[-.]?)?[6-9]\d{9}$'
        # Clean the number
        cleaned = re.sub(r'[\s\-\.]', '', phone)
        return bool(re.match(pattern, cleaned))

    @staticmethod
    def validate_postal_code(postal_code: str) -> bool:
        """Validate Indian postal code (6 digits)"""
        pattern = r'^\d{6}$'
        return bool(re.match(pattern, postal_code))

    @staticmethod
    def validate_driving_license(license_number: str) -> bool:
        """Validate Indian driving license format"""
        # Format: 2 letter state code + 10 digits
        pattern = r'^[A-Z]{2}\d{13}$'
        return bool(re.match(pattern, license_number))

    @staticmethod
    def validate_vehicle_registration(reg_number: str) -> bool:
        """Validate Indian vehicle registration format"""
        # Format: 2 letter state + 2 digit district + 2 letter series + 4 digits
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
        return bool(re.match(pattern, reg_number))


class SensitiveDataMasker:
    """Mask sensitive data for logging and storage"""

    @staticmethod
    def mask_phone(phone: str) -> str:
        """Mask phone number: 919876543210 -> 91****3210"""
        if len(phone) < 4:
            return phone
        return phone[:2] + "****" + phone[-4:]

    @staticmethod
    def mask_pan(pan: str) -> str:
        """Mask PAN: ABCDE1234F -> ABCDE****F"""
        if len(pan) < 4:
            return pan
        return pan[:5] + "****" + pan[-1:]

    @staticmethod
    def mask_aadhaar(aadhaar: str) -> str:
        """Mask Aadhaar: 123456789012 -> ****6789"""
        if len(aadhaar) < 4:
            return aadhaar
        return "****" + aadhaar[-4:]

    @staticmethod
    def mask_bank_account(account: str) -> str:
        """Mask bank account: show last 4 digits only"""
        if len(account) < 4:
            return account
        return "*" * (len(account) - 4) + account[-4:]

    @staticmethod
    def mask_email(email: str) -> str:
        """Mask email: john@example.com -> j***@example.com"""
        try:
            local, domain = email.split('@')
            if len(local) <= 1:
                masked_local = local[0] + "***"
            else:
                masked_local = local[0] + "***" + local[-1]
            return f"{masked_local}@{domain}"
        except ValueError:
            return email
