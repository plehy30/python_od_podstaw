light = input("Jakie widzisz światło? (zielone, żółte, czerwone)")

match light:
    case "zielone":
        print("możesz jechać")
    case "żółte":
        print("Przygotuj się")
    case "czerwone":
        print("Stój")
    case _:
        print("Nie znam takiego koloru")
