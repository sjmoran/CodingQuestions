'''
Sean Moran
sean.j.moran@gmail.com
'''
import numpy as np
from collections import defaultdict

class Partitioner():
    """
    My solution is a greedy algorithm that at a given step, selects the allocation 
    for a given user that maximises the entropy. A uniform distribution has maximum
    entropy and the model will try to each this maximum entropy state.

    This solution is a greedy non-optimal method that has O(NK) time complexity,
    where N is the number of records and K are the number of partitions. The
    memory requirement is O(N+K) to hold the allocations array and the records
    data structures in memory.
 
    Assumptions: None
    """

    def __init__(self, K):
        """Initialise the class with K, the number of required partitions

        :param K: number of partitions (integer) 
        :returns: N/A
        :rtype: N/A

        """
        if K<=0:
           raise Exception("Number of partitions (K) must be greater than 0")

        self.K=K
        
        self.records=defaultdict(list) 

    def _print_records(self):
        """Prints user records to standard out for inspection

        :returns: N/A
        :rtype: N/A

        """
        print("User ID, Records, Partition")
        for num_record, record_list in sorted(self.records.items(), reverse=True):
            for record in record_list:
                record.print_record()

    def _compute_entropy(self, allocations):
        """Computes the entropy of the record allocation array

        :param allocations: list of allocations for each partition 
        :returns: entropy
        :rtype: float

        """
        allocations=allocations/allocations.sum(axis=0, keepdims=True)
        entropy=(-allocations*np.log2(allocations)).sum(axis=0)
        return entropy

    def _add_records(self,records):
        """Adds user records to a dictionary data structure

        :param records: list of record objects
        :returns: N/A
        :rtype: N/A

        """
        for record in records:

            print("Adding record: %s, %d" % (record.user_id, record.num_records))

            if record.num_records>0:
                '''
                Seems sensible to only add records with a positive number of records
                '''
                self.records[record.num_records].append(record)
    
    def get_partitions(self, records):
        """ Greedy partitioning algorithm that attempts to maximise entropy
      
        :param records: Dictionary of lists, with each list element being a Record
        :returns: Assignment of each Record to a partition 
        :rtype: Dictionary of lists

        """
        if not records:
            '''
            Catch error case where no records are provided
            '''
            return self.partitions

        self._add_records(records)
        '''
        Greedily find the partitioning that maximises the entropy
        '''
        max_entropy=0
        allocations=np.zeros((self.K))+0.000000001 # small positive constant to prevent NaN
        
        for num_record, record_list in sorted(self.records.items(), reverse=True): # iterate over users, those with largest number of records first
           '''
           Add record to partition that maximises total entropy
           '''
           best_partition=-1

           for record in record_list:
               
            for j in range(0,self.K):

               '''
               Add user to partition j and compute entropy
               ''' 
               allocations[j]=allocations[j]+num_record
               entropy=self._compute_entropy(allocations)

               if j==0:
                   '''
                   If we are at the first partition reset max entropy
                   '''
                   max_entropy=entropy

               '''
               Record the partition with the highest entropy for this user
               '''
               if entropy >= max_entropy:
                   max_entropy=entropy
                   best_partition=j

               '''
               Remove the allocation for this user and test the next allocation
               '''
               allocations[j]=allocations[j]-num_record

            '''
            Add the user to the partition that had maximum entropy during our search
            '''
            record.partition=best_partition+1 # partition number is an integer in [1...K]
            allocations[best_partition]=allocations[best_partition]+num_record
            
        print("\nPartitions are: \n")     
        self._print_records()
        entropy=self._compute_entropy(allocations)
        print("Entropy of partitioning: " + str(entropy))
        return records 
    
class Record():
    '''
    Class that represents the user and their attributes (number records, user id and allocated partition)
    '''
    def __init__(self, num_records, user_id):
        """Object initialiser

        :param num_records: Number of records of user
        :param user_id: String user id
        :returns: N/A
        :rtype: N/A

        """
        self.num_records=num_records
        self.user_id=user_id
        self.partition=-1

    def print_record(self):
        """Prints the attributes of the object to standard output

        :returns: N/A
        :rtype: N/A

        """
        print("%s, %d, %d" % (self.user_id, self.num_records, self.partition))
        

        
def main():
    """Main function with some unit tests 

    :returns: N/A
    :rtype: N/A

    """

    '''
    Valid data test to check that a fairly uniform 
    partitioning is made
    '''
    record1=Record(20,"Sean")
    record2=Record(5,"Paul")
    record3=Record(5,"John")
    record4=Record(5,"Steve")
    record5=Record(15,"Jess")

    records=[]
    records.append(record1)
    records.append(record2)
    records.append(record3)
    records.append(record4)
    records.append(record5)
    
    partitioner = Partitioner(K=3)
    partition=partitioner.get_partitions(records)

    '''
    Invalid data test - Jess has invalid record number
    This should be handled by skipping the record
    '''
    record1=Record(20,"Sean")
    record2=Record(5,"Paul")
    record3=Record(5,"John")
    record4=Record(5,"Steve")
    record5=Record(-100,"Jess")

    records=[]
    records.append(record1)
    records.append(record2)
    records.append(record3)
    records.append(record4)
    records.append(record5)
    
    partitioner = Partitioner(K=2)
    partition=partitioner.get_partitions(records)

    '''
    Invalid data test, K cannot be less than 1
    '''
    '''
    partitioner = Partitioner(K=-1)
    '''
    
if __name__ == '__main__':
    main()   
     
