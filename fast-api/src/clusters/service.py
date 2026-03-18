
from sqlmodel import Session, select

from src.clusters.models import ClusterModel
from src.clusters.schemas import ClusterReq


class ClusterService:
    @staticmethod
    def get_all_clusters(session: Session):
        clusters = session.exec(select(ClusterModel)).all()
        return clusters
        

    @staticmethod
    def get_specific_cluster(cluster_id: int,session: Session):
        for i in clusterData:
            if i["id"] == cluster_id:
                return i

    @staticmethod
    def create_cluster_entry(clusterRequest: ClusterReq,session: Session):
        new_id = max([i["id"] for i in clusterData], default=0) + 1
        new_cluster_data = clusterRequest.model_dump()
        new_cluster_data["id"] = new_id
        clusterData.append(new_cluster_data)
        return new_cluster_data

    @staticmethod
    def update_cluster_entry(cluster_id: int, cluster_update_data: ClusterReq,session: Session):
        update_data = cluster_update_data.model_dump()

        for i in clusterData:
            if i["id"] == cluster_id:
                i.update(update_data)
                return i

    @staticmethod
    def delete_cluster_entry(cluster_id: int,session: Session):
        for i in clusterData:
            if i["id"] == cluster_id:
                clusterData.remove(i)
                return True

        return False
