from banking import BankManager

def main():
    manager = BankManager()

    while True:
        print("\n=== 🏦 Python Bank ATM ===")
        print("1. 계좌 개설 | 2. 입금 | 3. 출금 | 4. 잔액 조회 | 5. 종료")

        try:
            choice = input("선택: ").strip()

            if  choice == '1':
                acc_num = input("계좌번호를 입력하세요:")
                owner = input('사용자 이름을 입력하세요: ')
                acc_type= input('계좌 종류를 입력하세요.(normal: 일반 계좌, premium):')
                manager.create_account(acc_num,owner,acc_type)

            elif choice =='2':
                acc_num = input("계좌번호 :")
                my_acc = manager.get_account(acc_num)
                amount= int(input('입금액을 입력하세요'))
                my_acc.deposit(amount)

            elif choice =='3':
                acc_num = input("계좌번호 :")
                my_acc = manager.get_account(acc_num)
                amount= int(input('출금액을 입력하세요'))
                my_acc.withdraw(amount)

            elif choice == '4':
                acc_num = input("계좌번호 :")
                print(f'잔액 확인: {manager.get_account(acc_num)}')
            elif choice == '5':
                print('안녕히 가세요!')
                break
            else:
                print('잘못된 메뉴 선택입니다.')

        except ValueError as e:
            print(f'[입력/처리 오류] {e}')
        except KeyError as e:
            print(f'[계좌 오류] {e}')
        except Exception as e:
            print(f'[알 수 없는 오류] {e}')

if __name__ == "__main__":
    main()

            
