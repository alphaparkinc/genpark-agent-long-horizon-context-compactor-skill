from client import AgentLongHorizonContextCompactorClient

def main():
    client = AgentLongHorizonContextCompactorClient()
    res = client.compact_context_memory()
    print('Context Compactor: ' + res['compaction_id'] + ' (Ratio: ' + str(res['compression_ratio']) + 'x)')
    print('Tokens: ' + str(res['original_tokens']) + ' -> ' + str(res['compacted_tokens']) + ' | Facts: ' + str(res['extracted_episodic_facts_count']))
    print('Anchor Keys: ' + str(res['episodic_anchor_keys']))
    print('Memory Frame: ' + res['memory_frame_url'])

if __name__ == '__main__':
    main()
