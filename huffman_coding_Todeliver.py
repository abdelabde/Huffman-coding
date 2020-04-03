class HuffmanTree:
    """Classe représentant un arbre binaire"""

    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right =right

def get_frequencies(text):
    """:param text: un str qu'on veut compresser
         :return: une liste de tuples qui contiennent un caractère en premier position et
      sa frequence d'apparition dans text en second
     """
    Output=[]
    for character in text:
        c=True
        if Output==[]:
            Output.append((character,1))
        else:
            for x in range(len(Output)):
                (b,a)=Output[x]
                if character==b:
                    Output[x]=(b,a+1)
                    c=False
            if c==True:
                Output.append((character,1))
    return Output
   
def Combine(tree1,tree2):
    """Combine deux HuffmanTree arbres pour avoir un seul"""
    return HuffmanTree(freq=tree1.freq+tree2.freq,left=tree1,right=tree2)
    
def List_to_tree_nodes(freq_list):
    """Convertir une liste de tuples à une liste des noueds de  HuffmanTree arbre avec la meme information"""
    nodes = []
    for L in freq_list:
        nodes.append(HuffmanTree(L[1],L[0]))
    return nodes

def Build(nodes):
    if len(nodes) == 1:
        '''en bas s'il ne reste qu'un nœud'''
        return nodes[0]
    else:
        '''sinon trier la liste, prendre les deux derniers éléments et combiner'''
        nodes.sort(key = lambda x: x.freq, reverse=True)
        n1 = nodes.pop()
        n2 = nodes.pop()
        nodes.append(Combine(n2, n1))
        return Build(nodes)  
def build_huffman_tree(freq_list):
    """
    :param freq_list: la liste des frÃ©quences
    :return: une instance de HuffmanTree (l'arbre de huffman que vous avez construit)
    """
    nodes =List_to_tree_nodes(freq_list)
    return Build(nodes)

def convert_bin_string_to_bytes(compressed_text):
    """
    :param compressed_text: str composÃ© uniquement de "0" et "1"
    :return: bytes
    """
    padding = len(compressed_text) % 8
    if padding != 0:
        padding = 8 - padding

    byte_list = list()
    compressed_text += "0" * padding
    for i in range(0, len(compressed_text), 8):
        byte = compressed_text[i:i + 8]
        byte_list.append(int(byte, 2))
    return bytes(byte_list)

def flatten_to_dict(huffman_tree, codeword="", code_dict={}):
    """Parcourt l'arbre, construisant un dict avec les mots de code"""
    
    #bottom out - if symbol exists then the node is a leaf
    if huffman_tree.char:
        if codeword == "":
            #if there is no codeword passed to it yet, then source is 1 symbol
            codeword = "0"
        
        #by the time it gets to a leaf, codeword is constructed & can be added
        code_dict[huffman_tree.char] = codeword
    else:
        flatten_to_dict(huffman_tree.left, codeword+"0", code_dict)
        flatten_to_dict(huffman_tree.right, codeword+"1", code_dict)

    return code_dict

def chunker(seq, size):
    """Itère en morceaux"""
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def compress(text,coding):
    """
    :param huffman_tree: un arbre de huffman pouvant servir Ã  compresser text
    :param text: le texte Ã  compresser
    :return: un objet de type bytes, rÃ©sultant de la compression
    """
    EOT=chr(4)
    code_message = []
    for i in chunker(text, 1):
        #fill end of message with EOT symbols
        while not len(i) == 1:
            i += EOT
        code_message.append(coding[i])

    return "".join(code_message)

def convert_bytes_to_bin_string(compressed_binary):
    """
    :param compressed_binary: un objet de type bytes
    :return: str composé uniquement de "0" et "1"
    """
    compressed_text = ""
    for b in compressed_binary:
        compressed_text += f"{b:08b}"
    return compressed_text


def decompress(huffman_tree, compressed_binary):
    """
    :param huffman_tree: l'arbre de huffman correspondant au texte original
    :param compressed_binary: le texte compressÃ© sous forme de bytes
    :return: un objet de type str qui, si tout se passe bien, devrait correspondre au texte original.
    """
    decoded=[]
    t = huffman_tree
    for i in compressed_binary:
        if i == "0":
            t = t.left
        elif i == "1":
            t = t.right
        else:
            raise Exception("Code_message not binary")

        if t.char:
            decoded.append(t.char)
            t = huffman_tree

    return "".join(decoded)


def print_huffman_tree(huffman_tree):
    """
    :param huffman_tree: un objet de type HuffmanTree
    :return: None
    """
    if (huffman_tree != None) : 
        print_huffman_tree(huffman_tree.left)  
        if (huffman_tree.left != None and 
            huffman_tree.right != None) : 
            print(huffman_tree.freq, end = " ")  
        print_huffman_tree(huffman_tree.right)
    else:
        print(None)
  

