# Add necessary imports
from eth_abi import decode_abi
from eth_abi.exceptions import InsufficientDataBytes

def parse_contract(contract):
    """
    Parse the contract bytecode and return a more friendly format
    """
    try:
        print(f"\nContract: {contract}")
        print("\nDecompiling...\n")

        # Decompile the bytecode
        instructions = disassembler.disassemble(contract)

        # Print the decompiled instructions
        for instr in instructions:
            print(f"{instr['offset']:04x}: {instr['opcode']} {instr['operand']}")

    except InsufficientDataBytes as e:
        print("\n[ERROR] - Could not decode contract: {0}\n".format(str(e)))

# Use an example contract
bytecode = "0x608060405234801561001057600080fd5b5061013f806100206000396000f3fe608060405234801561001057600080fd5b50600436106100535760003560e01c806361bc221a1461005857806367e404ce146101025780637135ff2f146101395780637c82625214610162578063bfaf92961461018a578063fb1652df146101ae575b600080fd5b6100606101c7565b60405161006d9190610582565b60405180910390f35b6100ee60048036038101906100e9919061047c565b610219565b6040516100fb919061056e565b60405180910390f35b61011f600480360381019061011a9190610457565b610260565b60405161012c9190610582565b60405180910390f35b61016e60048036038101906101699190610499565b610269565b60405161017b919061056e565b60405180910390f35b6101b860048036038101906101b39190610499565b610541565b6040516101c5919061058f565b60405180910390f35b6101ef60048036038101906101ea919061042c565b6105a7565b005b600060208282548352604080870152602001838152549051948316808284378201915050945050505050565b3490507ff4fdf300000000000000000000000000000000000000000000000000000000000816040516040519081906020015060405190810160405280608101905060206040820181815283526064906001830190508054620f42409081160281526020810191829003601401902091509190819003608401902060c08103846106ee565b6000818152602081905260409020546001600160a01b031681565b6000818152602081905260409020546001600160a01b0316331461027957600080fd5b506001600160a01b0382163373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461086c90919063ffffffff16565b60008282604051602001808383808284378083019250505092505050604051602081830303815290604052805190602001206204a480850304828501526020820190506020604082018181529350696e7365727400000000000000000000000000000000000000000000000000000897f8a8e84c000000000000000000000000000000000000000000000000000000000141796ddf311a149a4064b8a7a29bd9fdf7177f064153f71c2fb3c469f55a157aa466ffffffffffffffffffffffffffffffffffffffff166c010000000000000000000000000000000000000000000000000000000063ffffffff9081163065640204179092550a8f929093024260400a8204610a3b91908101906105eb565b600033905090565b5060005b8381101561033457600083815260200160208202805190602001206001600160a01b0316101561031057600080fd5b819050919050565b3390565b5060006003546001600160a01b0316331461035557600080fd5b5060005b838110156104dd5760018481526020016001820280519060200120620f42408683030482850152858552602082019050602060020a600014156104ce57600080fd5b8083116104bd57600080fd5b815194909352505050565b6001600160a01b031660009081526020819052604090205490565b600081606061052f84610587565b91506080826001600160a01b0316610a3b91908101906105eb565b62015180346108d790919063ffffffff16565b6000818152602081905260409020546001600160a01b031681565b60008282018381101561057d57fe5b9392505050565b60006105aa85856105ad565b825b905092915050565b60008181526020811415156105c657600080fd5b60208201915050919050565b6000818152602081905260408120549091506001600160a01b0391821693509182029190910460ff1690565b600061061a610619846105ad565b8989898833916388890211610619585b838b938b938b9b038b6040518181016040528060008152506204a4808603040183015286204a480861483019350600061071090910201916109c7565b3390505b919050565b7f8cfcd92a40000000000000000000000000000000000000000000000000000000081565b61071982826108f7565b6107228282610909565b5050565b7f49a042650000000000000000000000000000000000000000000000000000000081565b6000818152602081905260409020546001600160a01b0316331461075057600080fd5b506000805473ffffffffffffffffffffffffffffffffffffffff1916336001600160a01b03169052565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061079757805160ff19168380011785556107c5565b828001600101855582156107c5579182015b828111156107c45782518255916020019190600101906107a9565b506107d19291506107d5565b5090565b61070791905b808211156107d15760008160009055506001016107b9565b5090565b90565b7f4b170b770000000000000000000000000000000000000000000000000000000811565b6107438282610937565b61074c8282610941565b610755828261095b565b61075e828261096f565b6107678282610983565b610770828261098e565b60006001600160a01b0382161561078f57600080fd5b600080546001600160a01b0319166001600160a01b0392909216919091179055565b6107b48282610944565b156107bf576040516001600160a01b03821690825260048201929082606001516001600160a01b0316815260200134905050610a3b91908101906105eb565b6107f58282610944565b600061080482826108cd565b915081905092915050565b60006060826001600160a01b038416600090815260208190526040902054805160206108478284610983565b9150509392505050565b60008181526020819052604090205461086e908263ffffffff6109c516565b600081815260208190526040902054610893908263ffffffff6109e716565b848110156108ba57815160009081526006602052604090208290555b919050565b60075460009062015180019250620f4240810191029050838211156108ee576040516001600160a01b03808516908380156108ef575080155b156108f857600080fd5b92919050565b886001600160a01b031661090078846108d7565b34801561091857600080fd5b5060408051602061092f9181018085019060200160208301526202b36882420160248201528101602060020a05436108e09091020191610a61565b34801561096657600080fd5b5060408051602061098181810183019060200160208301526202b36882420160248201528101602060020a05436108e09091020191610a61565b3480156109ad57600080fd5b506109b6610541565b6040516109c3919061058f565b60405180910390f35b7f6c44af770000000000000000000000000000000000000000000000000000000081565b60008181526020811415156109ef57600080fd5b60208201915050919050565b610a0183836108f7565b348015610a0d57600080fd5b50602060020a610a1883836108b6565b9392505050565b60008215610a375760009150610a90565b50808402016040519080825280601f01601f191660200182016040528015610a71576020820182015260200161620fd4565b509350505050600060405180830381855af49150503d8060008114610aa4576040519150601f19603f3d011682016040523d82523d6000602084013e610aa9565b606091505b509150915081610aef5760405162461bcd60e51b815260040190806040018281038252602781526020018061125c6027913960400191505060405180910390fd5b859350610afc81600a620f42408302610a7b565b600060405180830381855af49150503d8060008114610b30576040519150601f19603f3d011682016040523d82523d6000602084013e610b35565b606091505b509150915081610b7a5760405162461bcd60e51b815260040190806040018281038252603581526020018061123b6035913960400191505060405180910390fd5b859350610b8781600a620f42408302610b67565b600060405180830381855af49150503d8060008114610bbe576040519150601f19603f3d011682016040523d82523d6000602084013e610bc3565b606091505b509150915081610c035760405162461bcd60e51b81526004019080604001828103825260348152602001806111f86034913960400191505060405180910390fd5b6040516001600160a01b0316907f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92590600090a36001805473ffffffffffffffffffffffffffffffffffffffff19166001600160a01b0392909216919091179055565b600082821115610c6557505050565b5080820391505092915050565b8033141515610c8157600080fd5b818303905092915050565b600082820183811015610ca657fe5b92915050565b600082820183811015610cb757fe5b805182526020831115610cb757602082019150602081019050602083039250610c9357600080fd5b5050505050565b60020a60008383610ced5750805b82811015610cff5760008481526020015060208202805190602001208361c350610ce257fe5b805182526020831115610ce257602082019150602081019050602083039250610d5e565b5050505050565b600160a01b038216600090815260208190526040902054610dbf908463ffffffff6109c516565b600160a01b03831660008281526020818152604080832093861680845294832054909290829020859055815185815293516001600160a01b039092169163a9059cbb9160448083019260209291908290030181600088803b158015610e39573d6000803e3d6000fd5b505af1158015610e4d573d6000803e3d6000fd5b5050505050565b7f547e65e50000000000000000000000000000000000000000000000000000000081565b60008080610e73826001610f6f565b92915050565b60006020820190508181036000830152610e9281610c05565b9050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b60008282526020820190508181036000830152610ef481610cf5565b9050919050565b600082825260208201905092915050565b6000602082019050610f226000830184610d17565b92915050565b6000602082019050610f3d6000830184610d17565b92915050565b6000602082019050610f586000830184610d17565b92915050565b60006020820190508181036000830152610f7b81610d3e565b9050919050565b60006020820190508181036000830152610f9e81610d56565b9050919050565b60006020820190508181036000830152610fc181610d6e565b9050919050565b60006020820190508181036000830152610fe481610d86565b9050919050565b6000602082019050818103600083015261100781610d9e565b9050919050565b6000602082019050818103600083015261102a81610db6565b9050919050565b6000602082019050818103600083015261104d81610dce565b9050919050565b6000602082019050818103600083015261107081610de6565b9050919050565b6000602082019050818103600083015261109381610dfe565b9050919050565b600060208201905081810360008301526110b681610e16565b9050919050565b600060208201905081810360008301526110d981610e2e565b9050919050565b600060208201905081810360008301526110fc81610e46565b9050919050565b6000602082019050818103600083015261111f81610e5e565b9050919050565b6000602082019050818103600083015261114281610e76565b9050919050565b6000602082019050818103600083015261116581610ec6565b9050919050565b6000602082019050818103600083015261118881610edc565b9050919050565b61019880611062565050506101f0565b61019880611062565050506101f0565b61019880611004465050506101f0565b6101988061109a4650050506101f0565b6101998061109a5750506101f0565b61019880611062565050506101f0565b61019880611062565050506101f0565b61019880611062565050506101f0565b61019880611062565050506101f0565b6101998061103a5750506101f0565b6101998061103a5750506101f0565b610199806110a45750506101f0565b610199806110a45750506101f0565b6101988061106256505050610284565b6101988061106256505050610284565b61019880611062565050506101f0565b61019880611062465050506101f0565b6101998061103a5750506101f0565b61019880611062465050506101f0565b610199806110b05750506101f0565b61019880611062465050506101f0565b61019880611062465050506101f0565b61019880611001465050506101f0565b6101998061107e5750506101f0565b6101998061107e5750506101f0565b6101998061107e5750506101f0565b6101998061107e5750506101f0565b6101998061107e5750506101f0565b61019880611001465050506101f0565b61019880611001465050506101f0565b61019880611001465050506101f0565b61019880611001465050506101f0565b610199806110c65750506101f0565b61019980611088575050610284565b61019880611001465050506101f0565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106112bd57805160ff19168380011785556112eb565b828001600101855582156112eb579182015b828111156112ea5782518255916020019190600101906112cf565b506112f79291506112fb565b5090565b61019891905b808211156112f75760008160009055506001016112df565b5090565b90565b6101c8806112056000396000f3fe6080604052600436106100b45760003560e01c80630b4d6b52146100ff5780631457b0ed1461101f5780638480081214611040578063f940e38514611060575b600454600160a01b900460ff16156100fd576002546040516370a0823160e01b81526001600160a01b0390911660048201819052600091606491906370a0823190602401602060405180830381865afa1580156100d7573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610b3e91906110da565b6100e091906110f9565b610b6f565b34801561010b57600080fd5b5061101461103e3660046111
