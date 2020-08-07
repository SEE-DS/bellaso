from bellaso import bellaso_encrypt, bellaso_decrypt

chosen_keyword = 'toddlovescopper'
demo = 'Nxwwkpf jrw qt ndy jxsv\nYrff ielwfpa ffnbgdcwzw\nLahs\'h drv aossj uvqw\n'

demo = bellaso_decrypt(demo, chosen_keyword)
print(f'A demonstration of Bellaso cipher DEcryption:\n{demo}')

to_encrypt = 'your message here!'
keyword = 'chooseyourownadventure'

encrypted_msg = bellaso_encrypt(to_encrypt, keyword)
print(f'\nA demonstration of Bellaso cipher ENcryption:\n{encrypted_msg}\n')