# Main class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.power_on = False

    def turn_on(self):
        if not self.power_on:
            self.power_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):
        if self.power_on:
            self.power_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def check_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh")


# Derived class 1
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version

    def check_specs(self):
        super().check_specs()
        print(f"Android Version: {self.android_version}")

    def install_app(self, app_name):
        print(f"Installing {app_name} from Google Play Store...")


# --- Example Usage ---
samsung = AndroidPhone("Samsung", "Galaxy S23", 256, 5000, "Android 14")

samsung.turn_on()
samsung.check_specs()
samsung.install_app("WhatsApp")
