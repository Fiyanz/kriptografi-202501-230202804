import random

class DiffieHellman:
    def __init__(
        self,
        p: int,
        g: int,
        name: str,
        private_key: int = None,
    ):
        self.p = p
        self.g = g
        self.name = name
        self.private_key = random.randint(1, p - 1) if private_key is None else private_key
        self.public_key = pow(g, self.private_key, p)
        self.shared_secret = None


    def compute_shared_secret(self, other_public_key: int):
        self.shared_secret = pow(other_public_key, self.private_key, self.p)
        return self.shared_secret


if __name__ == "__main__":

    p = 23  
    g = 5  

    A = 92378234
    B = 23482342

    # Alice's side
    alice = DiffieHellman(p, g, "Alice", private_key=A)
    print(f"Alice's Public Key: {alice.public_key}")

    # Bob's side
    bob = DiffieHellman(p, g, "Bob", private_key=B)
    print(f"Bob's Public Key: {bob.public_key}")

    # Compute shared secrets
    alice_shared_secret = alice.compute_shared_secret(bob.public_key)
    bob_shared_secret = bob.compute_shared_secret(alice.public_key)

    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"