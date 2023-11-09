

class PeselCheck:
    def correct_pesel(self, pesel):
        pesel_list = [int(i) for i in str(pesel)]
        control_sum = 0
        control_sum += pesel_list[0] * 1
        control_sum += pesel_list[1] * 3
        control_sum += pesel_list[2] * 7
        control_sum += pesel_list[3] * 9
        control_sum += pesel_list[4] * 1
        control_sum += pesel_list[5] * 3
        control_sum += pesel_list[6] * 7
        control_sum += pesel_list[7] * 9
        control_sum += pesel_list[8] * 1
        control_sum += pesel_list[9] * 3
        control_sum += pesel_list[10] * 1

        if control_sum % 10:
            return "NIE"
        else:
            return "TAK"

    def is_male(self, pesel):
        sex_digit = (pesel // 10) % 10
        return sex_digit % 2

    def get_birth_from_pesel(self, pesel):
        pesel_string = str(pesel)
        year_number = int(pesel_string[:2])
        month_number = int(pesel_string[2:4])
        day_number = int(pesel_string[4:6])
        if month_number > 80:
            month_number -= 80
            year_number += 1800
        elif month_number > 60:
            month_number -= 60
            year_number += 2200
        elif month_number > 40:
            month_number -= 40
            year_number += 2100
        elif month_number > 20:
            month_number -= 20
            year_number += 2000
        else:
            year_number += 1900

        return f"{day_number:02}-{month_number:02}-{year_number}"

