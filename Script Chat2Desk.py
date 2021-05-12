class Handler:
  #
  # new message handler
  #
  def new_message_handler(self, input_data, c2d):
    # This returns client id for every message received. The id is sent in system message, which is not seen by the client. To enable, turn on 'Incoming messages' option above.
    # Use this id for receiving logs of your script: text to connected messenger account and see your id, which you have to enter into Logging section below.
    c2d.send_message(input_data['client']['id'], "This client's id: " + str(input_data['client']['id']) + ".\n\n To turn off this message go to Settings/Script (under admin) and turn off 'Incoming messages' option.", "system")
    return input_data

  #
  # before sending message handler
  #
  def before_sending_message_handler(self, input_data, c2d):
    return '[before_sending_message] do logic here'

  #
  # after closing dialog handler
  #
  def after_closing_dialog_handler(self, input_data, c2d):
    return '[after_closing_dialog] do logic here'

  #
  # before closing dialog handler
  #
  def before_closing_dialog_handler(self, input_data, c2d):
    return '[after_closing_dialog] do logic here'

  #
  # auto checking handler
  #
  def auto_checking_handler(self, input_data, c2d):
    return '[auto_checking] do logic here'
    return '[after_closing_dialog] do logic here'

  #
  # after scanning QR-code handler
  #
  def qr_code_result_handler(self, input_data, c2d):
    return '[qr_code_result] do logic here'

  #
  # after manually call
  #
  def manually_handler(self, input_data, c2d):
    return '[manually] do logic here'

  #
  # after chat bot don't triggered
  #
  def chat_bot_not_triggered_handler(self, input_data, c2d):
    return '[manually] do logic here'

  #
  # dialog transfer handler
  #
  def dialog_transfer_handler(self, input_data, c2d):
    return '[dialog_transfer] do logic here'

  #
  # new request handler
  #
  def new_request_handler(self, input_data, c2d):
    return '[new_request] do logic here'

  #
  # client updated handler
  #
  def client_updated_handler(self, input_data, c2d):
    return '[client_updated] do logic here'

  #
  # add_tag_to_request handler
  #
  def add_tag_to_request_handler(self, input_data, c2d):
    return '[add_tag_to_request] do logic here'

  #
  # delete_tag_from_request handler
  #
  def delete_tag_from_request_handler(self, input_data, c2d):
    return '[delete_tag_from_request] do logic here'

# examples
# send message
#response = c2d.send_message(94212, 'test!!!')

# send question
#response = c2d.send_question(94212, 4321)

# get client info
#response = c2d.get_client_info(94212)

# get operators
#response = c2d.get_operators()

# get online operators
#response = c2d.get_online_operators()

# get list of question
#response = c2d.get_questions(5369, '10-10-2015', '10-10-2016')

# get last question
# response = c2d.get_last_question(5369)

# get unanswered dialogs
#response = c2d.get_unanswered_dialogs(18000)

# transfer dialog
#response = c2d.transfer_dialog(81984, 1899)

# get last message id in dialog
# dialog_id = 100
# type = 2 (1-client, 2-operator, 3-auto, 4-system)
# 2*24*60*60 time ago
#response = c2d.get_last_message_id(100, 2, 2*24*60*60)

# operator groups_ids
# operator_id = 81984
#response = c2d.get_operator_group_ids(81984)

# check if operator in group
# operator_id = 81984
# group_id = 81984
#response = c2d.operator_in_group(81984, 100)

# not send menu in new_message_handler add
# print 'not send menu'
        