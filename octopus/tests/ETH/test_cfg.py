import unittest

from octopus.analysis.graph import CFGGraph
from octopus.platforms.ETH.cfg import EthereumCFG


class EthereumCfgTestCase(unittest.TestCase):

    # bytecode_hex = "60606040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680631b0ca26a146100725780635fd8c71014610087578063c0e317fb1461009c578063c6dd98e9146100a6578063f8b2cb4f146100bb575b600080fd5b341561007d57600080fd5b610085610108565b005b341561009257600080fd5b61009a6101cd565b005b6100a461028c565b005b34156100b157600080fd5b6100b96102da565b005b34156100c657600080fd5b6100f2600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061039e565b6040518082815260200191505060405180910390f35b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905060008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff168160405160006040518083038185876187965a03f19250505015156101ca57600080fd5b50565b3373ffffffffffffffffffffffffffffffffffffffff166000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205460405160006040518083038185876187965a03f192505050151561024657600080fd5b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550565b346000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550565b3373ffffffffffffffffffffffffffffffffffffffff166108fc6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549081150290604051600060405180830381858888f19350505050151561035857600080fd5b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490509190505600a165627a7a723058206c96ec820703e283140b2d7ca433b45ae2c81843758e0758913918dce06d26630029"
    bytecode_hex = "60606040526000357c0100000000000000000000000000000000000000000000000000000000900480635fd8c7101461004f578063c0e317fb1461005e578063f8b2cb4f1461006d5761004d565b005b61005c6004805050610099565b005b61006b600480505061013e565b005b610083600480803590602001909190505061017d565b6040518082815260200191505060405180910390f35b3373ffffffffffffffffffffffffffffffffffffffff16611111600060005060003373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060005054604051809050600060405180830381858888f19350505050151561010657610002565b6000600060005060003373ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600050819055505b565b34600060005060003373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828282505401925050819055505b565b6000600060005060008373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000505490506101b6565b91905056"
    cfg = EthereumCFG(bytecode_hex)

    number_func = 4
    number_instr = 231
    number_basicblock = 19
    edges = 18

    # visualization
    #graph = CFGGraph(cfg)
    #graph.view()

    def testInstructions(self):

        self.assertEqual(len(self.cfg.instructions), self.number_instr)

    def testEnumerateFunctions(self):

        self.assertEqual(len(self.cfg.functions), self.number_func)

    def testEnumerateBasicBlocks(self):

        self.assertEqual(len(self.cfg.basicblocks), self.number_basicblock)

    def testEdges(self):

        self.assertEqual(len(self.cfg.edges), self.edges)


class EthereumCfgTestCaseSimple(EthereumCfgTestCase):
    # simplecontract
    bytecode_hex = "6060604052341561000f57600080fd5b60d38061001d6000396000f3006060604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c14606e575b600080fd5b3415605857600080fd5b606c60048080359060200190919050506094565b005b3415607857600080fd5b607e609e565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820e1f98c821c12eea52047d7324b034ddccc41eaa7365d369b34580ab73c71a8940029"
    cfg = EthereumCFG(bytecode_hex)

    # result
    number_instr = 104
    number_func = 3
    number_basicblock = 15
    edges = 14

    # visualization
    # graph = CFGGraph(cfg)
    # graph.view()
    # graph.view_functions(simplify=True)


class EthereumSymbolicExecutionTestCaseMedium(EthereumCfgTestCase):

    bytecode_hex = "606060405260008080556001819055600a60025561012c60035560048190556109db90819061002d90396000f3606060405236156100b95760e060020a600035046309dfdc7181146100dd578063253459e31461011c5780634229616d1461013d57806357d4021b1461017857806367f809e9146101b7578063686f2c90146101ce5780636fbaaa1e146101fa5780638a5fb3ca1461022e5780639dbc4f9b14610260578063a26dbf26146102ed578063a6f9dae1146102f5578063b402295014610328578063ced9267014610366578063d11f13df1461039e578063fae14192146103ab575b6103d66103d86000670de0b6b3a76400003410156104755760018054340190555b50565b6040805160208181018352600080835283519054610100820190945260ca8082526103da94670de0b6b3a7640000900493926107d29083013990509091565b600154670de0b6b3a764000090045b60408051918252519081900360200190f35b6103d6600435600554600090600160a060020a039081163390911614156105955760015481148061016e5750606482115b1561055a57610002565b61012b6000670de0b6b3a7640000600660005060046000505481548110156100025792526002919091026000805160206109bb83398151915201540490565b6103d660058054600160a060020a03191633179055565b6103d65b600554600160a060020a039081163390911614156103d857600154600014156104ef57610002565b6103da6040805160208181018352600082528251600354610140820190945261011f808252909161089c9083013990509091565b6103da604080516020818101835260008252825160025460c082019094526084808252909161074e9083013990509091565b61044f600435600654600090819083116102e85760068054849081101561000257508054818352600285027ff652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f0154600160a060020a03169350670de0b6b3a764000091908590811015610002575050600284026000805160206109bb83398151915201540490505b915091565b60065461012b565b6103d6600435600554600160a060020a039081163390911614156100da5760058054600160a060020a0319168217905550565b6103d6600435600554600160a060020a039081163390911614156100da57600154670de0b6b3a76400009190910290811115610519576105196101d2565b6103d6600435600554600160a060020a039081163390911614156100da5761012c8111806103945750607881105b1561059957610002565b600654600454900361012b565b6103d660043560055433600160a060020a03908116911614156100da57600a81111561059e57610002565b005b565b60405180838152602001806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156104405780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b6040518083600160a060020a031681526020018281526020019250505060405180910390f35b506002546802b5e3af16b1880000341061048e57600290045b6100da816000600660005080548060010182818154818355818115116105a3576002028160020283600052602060002091820191016105a391905b80821115610607578054600160a060020a031916815560006001919091019081556104c9565b600154600554604051600160a060020a03919091169160009182818181858883f150505060015550565b6001546000141561052957610002565b600554604051600160a060020a039190911690600090839082818181858883f1505060018054919091039055505050565b506001546005546040516064909204830291600160a060020a039190911690600090839082818181858883f150506001805491909103905550505b5050565b600355565b600255565b50505091909060005260206000209060020201600050604080518082019091523380825260035460643491909102046020929092018290528254600160a060020a0319161782556001919091015550600654600a141561060b5760c860035561061c565b5090565b6006546019141561061c5760966003555b6000805460648481033490810282900490920190925560018054918502929092040190555b600454600680549091908110156100025760009182526002027ff652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f0190506001015460005411156105955760045460068054909190811015610002576002026000805160206109bb8339815191520154600454825491935090811015610002576002027ff652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d3f0154604051600160a060020a03919091169150600090839082818181858883f19350505050506006600050600460005054815481101561000257600091825281546002919091026000805160206109bb8339815191520154900390556004805460010190556106415653686f776e20696e202520666f726d2e204665652069732068616c766564283530252920666f7220616d6f756e747320657175616c206f722067726561746572207468616e203530206574686572732e2028466565206d6179206368616e67652c206275742069732063617070656420746f2061206d6178696d756d206f662031302529416c6c2062616c616e63652076616c75657320617265206d6561737572656420696e204574686572732c206e6f746520746861742064756520746f206e6f20646563696d616c20706c6163696e672c2074686573652076616c7565732073686f7720757020617320696e746567657273206f6e6c792c2077697468696e2074686520636f6e747261637420697473656c6620796f752077696c6c206765742074686520657861637420646563696d616c2076616c756520796f752061726520737570706f73656420746f54686973206d756c7469706c696572206170706c69657320746f20796f7520617320736f6f6e206173207472616e73616374696f6e2069732072656365697665642c206d6179206265206c6f776572656420746f2068617374656e207061796f757473206f7220696e63726561736564206966207061796f75747320617265206661737420656e6f7567682e2044756520746f206e6f20666c6f6174206f7220646563696d616c732c206d756c7469706c696572206973207831303020666f722061206672616374696f6e616c206d756c7469706c69657220652e672e203235302069732061637475616c6c79206120322e3578206d756c7469706c6965722e20436170706564206174203378206d617820616e6420312e3278206d696e2ef652222313e28459528d920b65115c16c04f3efc82aaedc97be59f3f377c0d40"
    cfg = EthereumCFG(bytecode_hex)

    # result
    number_instr = 1353
    number_func = 15
    number_basicblock = 99
    edges = 122

    # visualization
    # graph = CFGGraph(cfg)
    # graph.view()
    # graph.view_functions(simplify=True)

'''
class EthereumSymbolicExecutionTestCaseBig(EthereumCfgTestCase):

    # Ponzicoin
    bytecode_hex = "60606040526509184e72a000600355650246139ca800600455620186a060055573506a24fbcb8eda2ec7d757c943723cfb32a0682e600660006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550341561007f57600080fd5b62030d40600080600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555062030d40600260008282540192505081905550610f56806101096000396000f3006060604052600436106100db576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806306fdde03146100e0578063095ea7b31461016e57806318160ddd146101c857806323b872dd146101f15780632e1a7d4d1461026a578063313ce567146102a55780634b750334146102d45780634d853ee5146102fd57806370a08231146103525780638620410b1461039f57806395d89b41146103c8578063a9059cbb14610456578063b60d4288146104b0578063dd62ed3e146104d2578063eac037b21461053e575b600080fd5b34156100eb57600080fd5b6100f3610567565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610133578082015181840152602081019050610118565b50505050905090810190601f1680156101605780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561017957600080fd5b6101ae600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919080359060200190919050506105a0565b604051808215151515815260200191505060405180910390f35b34156101d357600080fd5b6101db610692565b6040518082815260200191505060405180910390f35b34156101fc57600080fd5b610250600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610698565b604051808215151515815260200191505060405180910390f35b341561027557600080fd5b61028b600480803590602001909190505061098e565b604051808215151515815260200191505060405180910390f35b34156102b057600080fd5b6102b8610a8f565b604051808260ff1660ff16815260200191505060405180910390f35b34156102df57600080fd5b6102e7610a94565b6040518082815260200191505060405180910390f35b341561030857600080fd5b610310610a9a565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561035d57600080fd5b610389600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610ac0565b6040518082815260200191505060405180910390f35b34156103aa57600080fd5b6103b2610b08565b6040518082815260200191505060405180910390f35b34156103d357600080fd5b6103db610b0e565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561041b578082015181840152602081019050610400565b50505050905090810190601f1680156104485780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561046157600080fd5b610496600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610b47565b604051808215151515815260200191505060405180910390f35b6104b8610d2a565b604051808215151515815260200191505060405180910390f35b34156104dd57600080fd5b610528600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610e9d565b6040518082815260200191505060405180910390f35b341561054957600080fd5b610551610f24565b6040518082815260200191505060405180910390f35b6040805190810160405280600981526020017f506f6e7a69436f696e000000000000000000000000000000000000000000000081525081565b600081600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a36001905092915050565b60025481565b6000816000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410158015610764575081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410155b80156107ed57506000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054826000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401115b1561098257816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540192505081905550816000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a360019050610987565b600090505b9392505050565b600080826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101515610a845760045483029050826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540392505081905550826002600082825403925050819055503373ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051600060405180830381858888f193505050501515610a7b57600080fd5b60019150610a89565b600091505b50919050565b600381565b60045481565b600660009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b60035481565b6040805190810160405280600381526020017f534543000000000000000000000000000000000000000000000000000000000081525081565b6000816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410158015610c1457506000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054826000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401115b15610d1f57816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540392505081905550816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a360019050610d24565b600090505b92915050565b600080600060035434811515610d3c57fe5b049150600554821115610d4f5760055491505b60035482029050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055503373ffffffffffffffffffffffffffffffffffffffff167f9cb9c14f7bc76e3a89b796b091850526236115352a198b1e472f00e91376bbcb836040518082815260200191505060405180910390a281600260008282540192505081905550816005600082825403925050819055506000600554111515610e4957620186a0600581905550600260036000828254029250508190555060026004600082825402925050819055505b80341115610e94573373ffffffffffffffffffffffffffffffffffffffff166108fc8234039081150290604051600060405180830381858888f193505050501515610e9357600080fd5b5b60019250505090565b6000600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b600554815600a165627a7a7230582016a9e20718c283abcd114dd550f5242bddfb719468e5296c821d3caa1924e68d0029"
    cfg = EthereumCFG(bytecode_hex)

    # result
    number_instr = 1894
    number_func = 16
    number_basicblock = 128
    edges = 140

    # visualization
    # graph = CFGGraph(cfg)
    # graph.view_ssa()
    # graph.view_functions(simplify=True)
'''
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EthereumCfgTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
