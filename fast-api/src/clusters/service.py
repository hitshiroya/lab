from sqlmodel import Session, select

from src.clusters.models import ClusterModel
from src.clusters.schemas import ClusterReq


class ClusterService:
    @staticmethod
    def get_all_clusters(session: Session):
        clusters = session.exec(select(ClusterModel)).all()
        return clusters

    @staticmethod
    def get_specific_cluster(cluster_name: str, session: Session):
        cluster = session.exec(select(ClusterModel).where(ClusterModel.name == cluster_name)).first()
        return cluster

    @staticmethod
    def create_cluster_entry(clusterRequest: ClusterReq, session: Session):
        new_cluster = ClusterModel(**clusterRequest.model_dump())
        session.add(new_cluster)
        session.commit()
        session.refresh(new_cluster)
        return new_cluster

    @staticmethod
    def update_cluster_entry(cluster_name: str, cluster_update_data: ClusterReq, session: Session):
        cluster = session.exec(select(ClusterModel).where(ClusterModel.name == cluster_name)).first()
        if not cluster:
            return None
        for key, value in cluster_update_data.model_dump().items():
            setattr(cluster, key, value)
        session.commit()
        session.refresh(cluster)
        return cluster

    @staticmethod
    def delete_cluster_entry(cluster_name: str, session: Session):
        cluster = session.exec(select(ClusterModel).where(ClusterModel.name == cluster_name)).first()
        if not cluster:
            return False
        session.delete(cluster)
        session.commit()
        return True
