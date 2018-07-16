import unittest
from unittest.mock import patch
from udp_chat.client import send_message

class TestClientUDPChat(unittest.TestCase):
    
#     def setUp(self):
#         self.uuid_patcher = patch('udp_chat.client.uuid4',
#                                   return_value='97b75429-5acf-40eb-963f-e712672b3e51')
#         self.uuid_patcher.start()

        
    @patch('udp_chat.client.uuid4', return_value='97b75429-5acf-40eb-963f-e712672b3e51')
    def test_send_message(self):
        ''' 
        username
        room_name
        room_password
        uuid
        datetime
        text
        refer_message
        '''
        
        uuid = send_message(username='luiz.zenon',
                            room_name='play',
                            room_password='parangari',
                            refer_message='5e203224-7d87-4917-9867-c7ca043a5a69',
                            message_text="Hello folks!,\nI'm testing this chat room")
        
        self.assertEqual(uuid, '97b75429-5acf-40eb-963f-e712672b3e51')            

if __name__ == '__main__':
    unittest.main()

