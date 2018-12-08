import sys

def decimal_tobinary(number):

    binary = 0
    i = 1
    while True:
        reminder = int(number)%2
        number /= 2
        binary += (reminder*i)
        i *= 10
        if(number == 0):
            break

    return binary

def subnet_calculator():

    try:
        print("Please enter IP address and Subnet mask in form(xxx.xxx.xxx.xxx).\n")
        while True:
            # Input IP you want to find
            input_ip = input("IP address: ")

            # split dot out from IP for checking in next step
            dotout_ip = input_ip.split(".")

            # add dotout_ip to array(in int type)

            intdotout_ip = []
            for i in dotout_ip:
                intdotout_ip.append(int(i))


            if (len(intdotout_ip) == 4):

                if (intdotout_ip[1] >= 0) and (intdotout_ip[1] <= 255):
                    if (intdotout_ip[2] >= 0) and (intdotout_ip[2] <= 255):
                        if (intdotout_ip[3] >= 0) and (intdotout_ip[3] <= 255):
                            break
            else:
                print("Error. <Invalid IP> Plese try again. \n")
                continue

        # Find class of IP address
        if 127 >= intdotout_ip[0] >= 1:
            class_ip = "Class A"
        elif 191 >= intdotout_ip[0] >= 128:
            class_ip = "Class B"
        elif 223 >= intdotout_ip[0] >= 192:
            class_ip = "Class C"
        else:
            class_ip = "Maybe Class D or E"



        # All possible of subnet masks can be
        posible_masks = [0, 128, 192, 224, 240, 248, 252, 254, 255]

        while True:

            # Input subnet mask
            input_subnet = input("Subnet mask: ")

            # split dot out from subnet mask for checking in next step
            dotout_subnet = input_subnet.split(".")

            # add dotout_subnet to array(in int type)
            intdotout_subnet = []
            for j in dotout_subnet:
                intdotout_subnet.append(int(j))


            if (len(intdotout_subnet) == 4):
                if intdotout_subnet[0] == 255:
                    if intdotout_subnet[1] in posible_masks and intdotout_subnet[2] in posible_masks and intdotout_subnet[3] in posible_masks:
                        if intdotout_subnet[0] >= intdotout_subnet[1] >= intdotout_subnet[2] >= intdotout_subnet[3]:
                            if 127 >= intdotout_ip[0] >= 1 and intdotout_subnet[1] >= 0 and intdotout_subnet[2] >= 0 and intdotout_subnet[3] >= 0:
                                break
                            elif 191 >= intdotout_ip[0] >= 128 and intdotout_subnet[1] == 255 and intdotout_subnet[2] >= 0 and intdotout_subnet[3] >= 0:
                                break
                            elif 223 >= intdotout_ip[0] >= 192 and intdotout_subnet[1] == 255 and intdotout_subnet[2] == 255 and intdotout_subnet[3] >= 0:
                                break
                            else:
                                print("Error. <Invalid Subnet mask with this class ip> Please try again. \n")
                                continue

            else:
                print("Error. <Invalid Subnet mask> Please try again. \n")
                continue



        # Change IP from decimal to binary by doing each 8 bit
        ip_tobinary = []
        ip_tobinary_each_eigthbit = []
        for i in intdotout_ip:
            i_binary = decimal_tobinary(i)
            ip_tobinary_each_eigthbit.append(str(i_binary))


        # Adding 0 in some IP binary number until. it's 8 bit
        #(Ex. binary of 5 = 101, this step will make 101 to 00000101)
        for i in range(0, len(ip_tobinary_each_eigthbit)):

            if len(ip_tobinary_each_eigthbit[i]) < 8:
                ip_after_adding_zero = ip_tobinary_each_eigthbit[i].zfill(8)
                ip_tobinary.append(ip_after_adding_zero)
            else:
                ip_tobinary.append(ip_tobinary_each_eigthbit[i])

        # use space(" ") to separate position in each 8bit of binary ip address
        ip_mask_binary = "".join(ip_tobinary)




        # Change Subnet mask from decimal to binary by doing each 8 bit
        sub_tobinary = []
        sub_tobinary_each_eightbit = []
        for j in intdotout_subnet:
            s_binary = decimal_tobinary(j)
            sub_tobinary_each_eightbit.append(str(s_binary))

        # Adding 0 in some Subnet msk binary number until. it's 8 bit
        # (Ex. binary of 5 = 101, this step will make 101 to 00000101)
        for i in range(0, len(sub_tobinary_each_eightbit)):

            if len(sub_tobinary_each_eightbit[i]) < 8:
                sub_after_adding_zero = sub_tobinary_each_eightbit[i].zfill(8)
                sub_tobinary.append(sub_after_adding_zero)
            else:
                sub_tobinary.append(sub_tobinary_each_eightbit[i])

        # use space(" ") to separate position in each 8bit of binary subnet mask address
        sub_mask_binary = "".join(sub_tobinary)



        # Find host number by using 2 pow number_sub_zero then - 2
        # Because max in each 8bit = 2 pow 7 but number_sub_zero count all 0. In max case = 8.
        # Then, number_host that use 2 pow number_sub_zero to calc. but 2 pow 8 is over max in each 8 bit
        # - 2 on it(like 2 pow 8 - 2 pow 1 = get 2 pow 7). Finally, you got number_host same is 2 pow 7 in this case.

        # number_sub_one = count 1 in subnet mask(Ex. 11111111.11111111.11111111.00000000 ,count 1 = 24)

        # number_sub_zero = count 0 in subnet mask,
        # in this case we already calc. number_sub_one that mean number_sub_zero = 32 - number_sub_one
        number_sub_one =  sub_mask_binary.count("1")
        number_sub_zero = 32 - number_sub_one
        number_hosts = abs((2 ** number_sub_zero) - 2)
        max_sub = str(2 ** abs(24 - number_sub_one))




        # Find Network address in binary
        network_addfront = ''

        for i in range(number_sub_one):
            network_addfront += ip_mask_binary[i]

        network_address = network_addfront + ("0" * int(number_sub_zero))


        #Change binary of network address/1st ip address back to decimal and add in to array
        network_pre_decimal = []
        network_temp_pre = ''
        firstadd_pre_ip = []

        cnet = 0
        lastp = 0
        for i in range(len(network_address)):

            cnet += 1
            network_temp_pre += network_address[i]

            if cnet == 8:
                if lastp == 3:
                    network_pre_decimal.append(str(int(network_temp_pre,2)))
                    firstadd_pre_ip.append(str(int(network_temp_pre, 2)+1))
                    network_temp_pre = ''
                    lastp = 0
                else:
                    network_pre_decimal.append(str(int(network_temp_pre, 2)))
                    firstadd_pre_ip.append(str(int(network_temp_pre, 2)))
                    network_temp_pre = ''
                    cnet = 0
                    lastp += 1

        #Use item in array to set in address form by adding "." each 8bit.
        network_decimal = ''
        for i in range(0, len(network_pre_decimal)):
            if i == 3:
                network_decimal += network_pre_decimal[i]
            else:
                network_decimal += network_pre_decimal[i] + "."

        firstadd_host_ip = ''
        for i in range(0, len(firstadd_pre_ip)):
            if i == 3:
                firstadd_host_ip += firstadd_pre_ip[i]
            else:
                firstadd_host_ip += firstadd_pre_ip[i] + "."





        # Find Broadcast address in binary
        broad_addfront = ''

        for i in range(number_sub_one):
            broad_addfront += ip_mask_binary[i]

        broad_address = broad_addfront + ("1" * int(number_sub_zero))

        # Change binary of broadcast address/last ip address back to decimal and add in to array
        broad_pre_decimal = []
        broad_temp_pre = ''
        lastadd_pre_ip = []

        cbroad = 0
        lastb = 0
        for i in range(len(broad_address)):

            cbroad += 1
            broad_temp_pre += broad_address[i]

            if cbroad == 8:
                if lastb == 3:
                    broad_pre_decimal.append(str(int(broad_temp_pre, 2)))
                    lastadd_pre_ip.append(str(int(broad_temp_pre, 2) - 1))
                    broad_temp_pre = ''
                    lastb = 0
                else:
                    broad_pre_decimal.append(str(int(broad_temp_pre, 2)))
                    lastadd_pre_ip.append(str(int(broad_temp_pre, 2)))
                    broad_temp_pre = ''
                    cbroad = 0
                    lastb += 1

        # Use item in array to set in address form by adding "." each 8bit.
        broad_decimal = ''
        for i in range(0, len(broad_pre_decimal)):
            if i == 3:
                broad_decimal += broad_pre_decimal[i]
            else:
                broad_decimal += broad_pre_decimal[i] + "."

        lastadd_host_ip = ''
        for i in range(0, len(lastadd_pre_ip)):
            if i == 3:
                lastadd_host_ip += lastadd_pre_ip[i]
            else:
                lastadd_host_ip += lastadd_pre_ip[i] + "."



        # All result
        print("\nThe entered ip address is: " + input_ip)
        print("The class of entered ip address is "+ class_ip)
        print("The entered subnet mask is: " + input_subnet)
        print("Number of subnet mask bits: " + str(number_sub_one))
        print("Number of hosts per subnet: " + str(number_hosts))
        print("Network address is: " + str(network_decimal))
        print("Broadcast address is: " + str(broad_decimal))
        print("IP address is: " + str(firstadd_host_ip) + " - " + str(lastadd_host_ip))
        print("Maximum number of subnets is: " + max_sub)
        list_ip = []

    except ValueError:
        print("Incorrect value. Please try again\n")

def loop_cal():
    while True:
        answer = input("Would you like to enter anymore IP's (y/n): ")
        if answer is 'y':
            subnet_calculator()
            continue
        elif answer is 'n':
            break
        else:
            print("Invalid answer!! Please try agian.\n")
            continue


# Calling the above defined function
if __name__ == '__main__':
    subnet_calculator()
    loop_cal()


  











