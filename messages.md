# Messages

## `0x00` HELLO

```python
{
  'network_id': 'uint8'
  'chain_id': 'uint8'
  'latest_finalized_root': 'bytes32'
  'latest_finalized_epoch': 'uint64'
  'best_root': 'bytes32'
  'best_slot': 'uint64'
}
```

## Ping / Pong

### `0x01` PING

This request has no body definition.

### `0x02` PONG

This response has no body definition.

## Block Root

### `0x10` REQUEST_BLOCK_ROOT

```python
{
  'start_root': 'bytes32'
  'start_slot': 'uint64'
  'max': 'uint64'
  'skip': 'uint64'
  'direction': 'uint8' # 0x01 is forward, 0x00 is backwards
}
```

### `0x11` SEND_BLOCK_ROOT

```python
[
  {
    'block_root': 'bytes32', 
    'slot': 'uint64'
  },
  …
]
```

## Block Header

### `0x12` REQUEST_BLOCK_HEADER

```python
{
  'start_root': 'bytes32'
  'start_slot': 'uint64'
  'max': 'uint64'
  'skip': 'uint64'
  'direction': 'uint8' # 0x01 is forward, 0x00 is backwards
}
```

### `0x13` SEND_BLOCK_HEADER

```python
{
    'slot': 'uint64',
    'parent_root': 'bytes32',
    'state_root': 'bytes32',
    'randao_reveal': 'bytes96',
    'eth1_data': Eth1Data,
    'signature': 'bytes96'
}
```

## Block Body

### `0x14` REQUEST_BLOCK_BODY

```python
{
  'start_root': 'bytes32'
  'start_slot': 'uint64'
  'max': 'uint64'
  'skip': 'uint64'
  'direction': 'uint8' # 0x01 is forward, 0x00 is backwards
}
```

### `0x15` SEND_BLOCK_BODY

```python
{
    'randao_reveal': 'bytes96',
    'eth1_data': Eth1Data,
    'proposer_slashings': [ProposerSlashing],
    'attester_slashings': [AttesterSlashing],
    'attestations': [Attestation],
    'deposits': [Deposit],
    'voluntary_exits': [VoluntaryExit],
    'transfers': [Transfer],
    'header_signature:' 'bytes96'
}
```

#### The following definitions are lined to v0.5.0 of the Beacon Chain Spec:

- [ProposerSlashing](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#proposerslashing)  
- [AttesterSlashing](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#attesterslashing)  
- [Attestation](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#attestation)  
- [Deposit](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#deposit)  
- [VoluntaryExit](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#voluntaryexit)  
- [Transfer](https://github.com/ethereum/eth2.0-specs/blob/v0.5.0/specs/core/0_beacon-chain.md#transfer)


