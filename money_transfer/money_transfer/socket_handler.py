import socket
from frappe import _
from money_transfer.money_transfer.utils import console_print
import sys

def make_socket_connection(ip, port, msg):
  error_msg = ''
  data = b''
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
      s.connect((ip, int(port)))
      s.sendall(msg)
      data = s.recv(2052)
      s.shutdown(socket.SHUT_RDWR)
    except socket.error:
      error_msg = _('Admin_ServerConnectionError')
    except:
      try:
        error_msg = str(sys.exc_info()[0])
      except:
        error_msg = ''
    finally:
      s.close()
  return data, error_msg