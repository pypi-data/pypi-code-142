import hashlib, random


class PasswordContext:
    itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def encode64(self, input: bytes, count: int) -> str:
        output = ""
        i = 0

        while i < count:
            value = input[i]
            i += 1
            output += self.itoa64[value & 0x3F]
            if i < count:
                value |= input[i] << 8
            output += self.itoa64[(value >> 6) & 0x3F]
            if i >= count:
                break
            i += 1
            if i < count:
                value |= input[i] << 16
            output += self.itoa64[(value >> 12) & 0x3F]
            if i >= count:
                break
            i += 1
            output += self.itoa64[(value >> 18) & 0x3F]

        return output

    def get_salt(self) -> str:
        random_bytes = random.randbytes(6)
        salt = self.encode64(random_bytes, 6)
        return salt

    def hash_password(self, password: str, salt: str) -> str:
        salt_bytes = salt.encode()
        password_bytes = password.encode()
        salt_password = salt_bytes + password_bytes

        m = hashlib.md5()
        m.update(salt_password)
        hash = m.digest()

        for _ in range(8192):
            m = hashlib.md5()
            hash_password = hash + password_bytes
            m.update(hash_password)
            hash = m.digest()

        hash = self.encode64(hash, 16)
        return hash

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        if len(hashed_password) < 12:
            return False

        salt = hashed_password[4:12]
        hash = self.hash_password(plain_password, salt)
        return hash == hashed_password[12:]

    def hash(self, password: str) -> str:
        salt = self.get_salt()
        hashed_password = "$P$B{}{}".format(salt, self.hash_password(password, salt))
        return hashed_password
