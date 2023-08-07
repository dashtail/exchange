class ClientInfo:
    def __init__(self, balance, limit):
        self.balance = balance
        self.limit = limit

    def apply_operation(self, operation):
        fx_quantity = operation["fx_quantity"]
        spot = operation["spot"]
        spread = operation["spread"]

        if operation["type"] == "In":
            operation_value = fx_quantity * (1 - spread) * spot

            if self.limit - operation_value < 0:
                return False
            
            self.balance += operation_value
            real_quantity = operation_value

        elif operation["type"] == "Out":
            operation_value = fx_quantity * (1 + spread) * spot
            
            if operation_value > self.limit:
                return False
            
            self.balance -= operation_value
            real_quantity = -operation_value

        self.limit -= operation_value
        if self.limit < 0:
            self.limit = 0

        operation["real_quantity"] = real_quantity

        return True


def process_operations(input_data):
    client_info = ClientInfo(input_data["balance"], input_data["limit"])
    processed_operations = []

    for operation in input_data["operations"]:
        if client_info.apply_operation(operation):
            processed_operations.append(
                {
                    "real_quantity": operation["real_quantity"],
                    "created_at": operation["created_at"],
                }
            )

    return {
        "client_info": {"balance": client_info.balance, "limit": client_info.limit},
        "operations": processed_operations,
    }
