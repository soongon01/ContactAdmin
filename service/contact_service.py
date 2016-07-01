"""

"""

def regist_contact(contact):
    """
    contact.dat 로 주소록을 관리한다.
    :param contact:
    :return:
    """
    #contact 객체를 스트링으로 변환
    # kim;010-3456-0000;kim@naver.com;seoul 변환해서 contact.dat 파일에 저장
    contact_str = contact.to_string()
    with open('contact.dat', 'a') as f:
        f.write(contact_str + '\n')





def view_all_contact():
    """
    [
        {
            "name"=name,
            "hpnum"=hpnum,
            "email"=email,
            "addr"=addr
        },
        {
            ..
        }
    ]
    :return: list
    """
    contact_list = []
    with open('contact.dat', 'r') as f:
        while True:
            line = f.readline()
            if not line: break;
            a_dic = _to_dic(line)
            contact_list.append(a_dic)

    return contact_list


def _to_dic(line):
    line = line[:-1] #맨 마지막 \n 제거
    dic = {}
    list = line.split(';')
    dic['name']  = list[0]
    dic['hpnum'] = list[1]
    dic['email'] = list[2]
    dic['addr']  = list[3]

    return dic


def modify_contact(contact):
    pass

def remove_contact(name):
    pass

def search_contact(name):
    pass




if __name__ == "__main__":
    print("실행 모듈이 아닙니다.")