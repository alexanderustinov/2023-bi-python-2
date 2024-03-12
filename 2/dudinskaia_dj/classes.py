class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def reverse_complement(self):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join([complement[base] for base in self.sequence][::-1])

    def gc_content(self):
        return (self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)
    
    def to_dict(self):
        return {"sequence": self.sequence}


class DNA(Sequence):
    def __init__(self, sequence):
        super().__init__(sequence)
    
    def transcription(self):
        return self.sequence.replace('T', 'U')

    def mutation(self, position, new_base):
        self.sequence = self.sequence[:position] + new_base + self.sequence[position+1:]

    def find_motif(self, motif):
        positions = []
        start = 0
        while True:
            start = self.sequence.find(motif, start)
            if start == -1: break
            positions.append(start)
            start += 1
        return positions
    
    def to_dict(self):
        base_dict = super().to_dict()
        return base_dict


class FASTAFile:
    def __int__(self, file_path):
        self.file_path = file_path

    def read_sequences(self):
        with open(self.file_path, 'r') as file:
            sequences = []
            sequence = ''
            for line in file:
                if not line.startswith('>'):
                    sequence += line.strip()
                else:
                    if sequence:
                        sequences.append(DNA(sequence))
                        sequence = ''
            if sequence:
                sequences.append(DNA(sequence))
            return sequences

    def write_sequence(self, dna_obj):
        with open(self.file_path, 'a') as file:
            file.write(f'>{dna_obj.sequence[:10]}...\n')
            file.write(dna_obj.sequence + '\n')