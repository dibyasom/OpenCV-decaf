class BeCalm(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "be calm bitch!"
        super().__init__(self.message+args[0])
