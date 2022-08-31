#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))
<<<<<<< HEAD
=======

>>>>>>> 39ea0f58beba6d4504d70fac5efaaa165829f255
