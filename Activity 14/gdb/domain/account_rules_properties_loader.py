from pathlib import Path


class AccountRulesPropertiesLoader:

    @staticmethod
    def load(account_type: str) -> dict:
        account_type = account_type.lower()

        rules_directory = (
            Path(__file__).resolve().parent.parent
            / "resources"
            / "config"
            / "rules"
        )

        file_path = rules_directory / f"{account_type}.properties"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Rules file not found: {file_path}"
            )

        rules = {}

        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                # Ignore empty lines and comments
                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    continue

                key, value = line.split("=", 1)

                rules[key.strip()] = value.strip()

        return rules

    @staticmethod
    def get_float(account_type: str, key: str, default: float = 0.0) -> float:
        rules = AccountRulesPropertiesLoader.load(account_type)

        value = rules.get(key)

        if value is None:
            return default

        return float(value)