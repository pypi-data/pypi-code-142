from typing import *
import torch
import abc
from torch import nn
from transformers import AutoModel, DistilBertModel
from .context import ContextHead, ContextTransformerAndWide
from .sequence import SequenceTransformerAEP, SequenceTransformerHistory
from transformers import DistilBertConfig, DistilBertModel
from vz_recommender.models.utils import MeanMaxPooling


class BST(nn.Module):
    """
    Args:
        deep_dims: size of the dictionary of embeddings.
        seq_dim: size of the dictionary of embeddings.
        seq_embed_dim: the number of expected features in the encoder/decoder inputs.
        deep_embed_dims: the size of each embedding vector, can be either int or list of int.
        seq_hidden_size: the dimension of the feedforward network model.
        num_wide: the number of wide input features (default=0).
        num_shared: the number of embedding shared with sequence transformer (default=1).
    """
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, wad_embed_dim, deep_embed_dims, seq_hidden_size,
                 num_wide=0, num_shared=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 page_embedding_weight=None, item_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__()
        context_head_kwargs = context_head_kwargs if context_head_kwargs else {}
        sequence_transformer_kwargs = sequence_transformer_kwargs if sequence_transformer_kwargs else {}
        if page_embedding_weight is None:
            print("not use pretrained page embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained page embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)

        if item_embedding_weight is None:
            print("not use pretrained item embedding")
            self.item_embedding = nn.Embedding(seq_dim, item_embed_dim)
        else:
            print("use pretrained item embedding")
            self.item_embedding = nn.Embedding.from_pretrained(item_embedding_weight, freeze=True)

        self.context_head = ContextHead(
            deep_dims=deep_dims,
            num_wide=num_wide,
            num_shared=num_shared,
            item_embedding=self.item_embedding,
            wad_embed_dim=wad_embed_dim,
            shared_embeddings_weight=shared_embeddings_weight,
            deep_embed_dims=deep_embed_dims
        )
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )
        self.dense1 = torch.nn.Linear(
            in_features=seq_embed_dim+2*wad_embed_dim,
            out_features=(seq_embed_dim+2*wad_embed_dim)//2
        )
        self.act1 = self.act2 = nn.LeakyReLU(0.2)
        self.dense2 = torch.nn.Linear((seq_embed_dim+2*wad_embed_dim)//2, seq_embed_dim)

    @abc.abstractmethod
    def forward(self, **kwargs):
        pass


class BSTBERT(BST):
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, deep_embed_dims, wad_embed_dim, seq_hidden_size, 
                 nlp_encoder_path, nlp_dim, nlp_embed_dim, num_wide=0, num_shared=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 item_embedding_weight=None, page_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__(deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, wad_embed_dim, 
                         deep_embed_dims, seq_hidden_size, num_wide, num_shared, context_head_kwargs, sequence_transformer_kwargs,
                         page_embedding_weight, item_embedding_weight, shared_embeddings_weight)
        self.nlp_encoder = AutoModel.from_pretrained(nlp_encoder_path)
        self.dense1 = torch.nn.Linear(
            in_features=seq_embed_dim+2*wad_embed_dim+nlp_embed_dim,
            out_features=(seq_embed_dim+2*wad_embed_dim+nlp_embed_dim)//2
        )
        self.dense2 = torch.nn.Linear((seq_embed_dim+2*wad_embed_dim+nlp_embed_dim)//2, seq_embed_dim)
        self.dense3 = torch.nn.Linear(seq_embed_dim, seq_dim)
        self.nlp_dense = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=nlp_embed_dim
        )

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, shared_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(**search_in).last_hidden_state[:,0,:].to(dtype=torch.float32)
        search_out = self.nlp_dense(search_out)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense3(user_out)
        return (outs, user_out)


class BSTAudienceTaWTT(nn.Module):
    def __init__(self, user_deep_dims, user_deep_embed_dims, user_num_wide, user_num_shared, user_wad_embed_dim,
                 offer_deep_dims, offer_deep_embed_dims, offer_num_wide, offer_num_shared, offer_wad_embed_dim,
                 svc_dim, svc_embed_dim, new_svc_dim, new_svc_embed_dim, page_dim, page_embed_dim, item_dim, 
                 item_embed_dim, seq_embed_dim, seq_hidden_size, nlp_encoder_path, nlp_dim=0, 
                 sequence_transformer_kwargs=None):
        super().__init__()
        # user layers
        self.user_context_head = ContextTransformerAndWide(
            deep_dims=user_deep_dims,
            num_wide=user_num_wide,
            deep_embed_dims=user_deep_embed_dims,
            wad_embed_dim=user_wad_embed_dim,
        )

        self.svc_embedding = nn.Embedding(svc_dim, svc_embed_dim)
        self.new_svc_embedding = nn.Embedding(new_svc_dim, new_svc_embed_dim)
        self.mm_pooling = MeanMaxPooling()

        self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        self.item_embedding = nn.Embedding(item_dim, item_embed_dim)
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )

        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        self.search_nlp_dense_0 = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=seq_embed_dim * 2
        )
        self.search_nlp_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim // 2
        )
        self.nlp_act = nn.LeakyReLU(0.2)

        if user_num_wide:
            user_ctx_out_dims = user_wad_embed_dim
        else:
            user_ctx_out_dims = user_wad_embed_dim // 2
        self.user_dense_0 = torch.nn.Linear(
            # nlp_out + aep_seq_out + svc_out + user_ctx_out
            in_features=seq_embed_dim // 2 + seq_embed_dim + svc_embed_dim * 2 + new_svc_embed_dim * 2 + user_ctx_out_dims,
            out_features=seq_embed_dim * 2
        )
        self.user_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim
        )
        self.user_act = nn.LeakyReLU(0.2)
        self.user_dropout = nn.Dropout(p=0.1)

        # offer layers
        self.offer_context_head = ContextTransformerAndWide(
            deep_dims=offer_deep_dims,
            num_wide=offer_num_wide,
            deep_embed_dims=offer_deep_embed_dims,
            wad_embed_dim=offer_wad_embed_dim,
        )

        if offer_num_wide:
            offer_ctx_out_dims = offer_wad_embed_dim
        else:
            offer_ctx_out_dims = offer_wad_embed_dim // 2
        self.offer_dense_0 = torch.nn.Linear(
            in_features=offer_ctx_out_dims,
            out_features=offer_ctx_out_dims + offer_ctx_out_dims // 2
        )
        self.offer_dense_1 = torch.nn.Linear(
            in_features=offer_ctx_out_dims + offer_ctx_out_dims // 2,
            out_features=seq_embed_dim
        )
        self.offer_act = nn.LeakyReLU(0.2)
        self.offer_dropout = nn.Dropout(p=0.1)

        self.out_act = nn.Sigmoid()

    def forward(self, user_deep_in, offer_deep_in, svc_in, new_svc_in, page_in, item_in, vl_in,
                user_wide_in=None, offer_wide_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        svc_out = self.svc_embedding(svc_in.long())
        svc_out = self.mm_pooling(svc_out)
        new_svc_out = self.new_svc_embedding(new_svc_in.long())
        new_svc_out = self.mm_pooling(new_svc_out)

        aep_seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)

        search_out = self.nlp_encoder(**search_in).last_hidden_state[:, 0, :].to(dtype=torch.float32)
        search_out = self.search_nlp_dense_0(search_out)
        search_out = self.nlp_act(search_out)
        search_out = self.search_nlp_dense_1(search_out)
        search_out = self.nlp_act(search_out)

        user_ctx_out = self.user_context_head(deep_in=user_deep_in, wide_in=user_wide_in)
        user_out = torch.cat([search_out, aep_seq_out, svc_out, new_svc_out, user_ctx_out], dim=1)
        user_out = self.user_dense_0(user_out)
        user_out = self.user_act(user_out)
        user_out = self.user_dropout(user_out)
        user_out = self.user_dense_1(user_out)
        user_out = self.user_act(user_out)

        offer_ctx_out = self.offer_context_head(deep_in=offer_deep_in, wide_in=offer_wide_in)
        offer_out = offer_ctx_out
        offer_out = self.offer_dense_0(offer_out)
        offer_out = self.offer_act(offer_out)
        offer_out = self.offer_dropout(offer_out)
        offer_out = self.offer_dense_1(offer_out)
        offer_out = self.offer_act(offer_out)

        out = torch.mul(user_out, offer_out)
        out = torch.sum(out, dim=1)
        out = self.out_act(out)

        return out, user_out, offer_out


class BSTAIALoyaltyTaWTT(nn.Module):
    def __init__(self, user_deep_dims, user_deep_embed_dims, user_num_wide, user_wad_embed_dim,
                 offer_deep_dims, offer_deep_embed_dims, offer_num_wide, offer_wad_embed_dim,
                 svc_dim, svc_embed_dim, new_svc_dim, new_svc_embed_dim, page_dim, page_embed_dim, item_dim,
                 item_embed_dim, seq_embed_dim, seq_hidden_size, nlp_encoder_path, nlp_dim=0,
                 sequence_transformer_kwargs=None):
        super().__init__()
        # user layers
        self.user_context_head = ContextTransformerAndWide(
            deep_dims=user_deep_dims,
            num_wide=user_num_wide,
            deep_embed_dims=user_deep_embed_dims,
            wad_embed_dim=user_wad_embed_dim,
        )

        self.svc_embedding = nn.Embedding(svc_dim, svc_embed_dim)
        self.new_svc_embedding = nn.Embedding(new_svc_dim, new_svc_embed_dim)
        self.mm_pooling = MeanMaxPooling()

        self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        self.item_embedding = nn.Embedding(item_dim, item_embed_dim)
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )

        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        self.search_nlp_dense_0 = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=seq_embed_dim * 2
        )
        self.search_nlp_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim // 2
        )
        self.nlp_act = nn.LeakyReLU(0.2)

        if user_num_wide:
            user_ctx_out_dims = user_wad_embed_dim
        else:
            user_ctx_out_dims = user_wad_embed_dim // 2
        self.user_dense_0 = torch.nn.Linear(
            # nlp_out + aep_seq_out + svc_out + user_ctx_out
            in_features=seq_embed_dim // 2 + seq_embed_dim + svc_embed_dim * 2 + new_svc_embed_dim * 2 + user_ctx_out_dims,
            out_features=seq_embed_dim * 2
        )
        self.user_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim
        )
        self.user_act = nn.LeakyReLU(0.2)
        self.user_dropout = nn.Dropout(p=0.1)

        # offer layers
        self.offer_context_head = ContextTransformerAndWide(
            deep_dims=offer_deep_dims,
            num_wide=offer_num_wide,
            deep_embed_dims=offer_deep_embed_dims,
            wad_embed_dim=offer_wad_embed_dim,
        )

        if offer_num_wide:
            offer_ctx_out_dims = offer_wad_embed_dim
        else:
            offer_ctx_out_dims = offer_wad_embed_dim // 2
        self.offer_dense_0 = torch.nn.Linear(
            in_features=offer_ctx_out_dims + seq_embed_dim // 2,
            out_features=offer_ctx_out_dims + offer_ctx_out_dims // 2
        )
        self.offer_dense_1 = torch.nn.Linear(
            in_features=offer_ctx_out_dims + offer_ctx_out_dims // 2,
            out_features=seq_embed_dim
        )
        self.offer_act = nn.LeakyReLU(0.2)
        self.offer_dropout = nn.Dropout(p=0.1)

        self.out_act = nn.Sigmoid()

    def forward(self, user_deep_in, offer_deep_in, svc_in, new_svc_in, page_in, item_in, vl_in,
                user_wide_in=None, offer_wide_in=None, search_in=None, offer_desc_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        svc_out = self.svc_embedding(svc_in.long())
        svc_out = self.mm_pooling(svc_out)
        new_svc_out = self.new_svc_embedding(new_svc_in.long())
        new_svc_out = self.mm_pooling(new_svc_out)

        aep_seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)

        search_out = self.nlp_encoder(**search_in).last_hidden_state[:, 0, :].to(dtype=torch.float32)
        search_out = self.search_nlp_dense_0(search_out)
        search_out = self.nlp_act(search_out)
        search_out = self.search_nlp_dense_1(search_out)
        search_out = self.nlp_act(search_out)

        offer_desc_out = self.nlp_encoder(**offer_desc_in).last_hidden_state[:, 0, :].to(dtype=torch.float32)
        offer_desc_out = self.search_nlp_dense_0(offer_desc_out)
        offer_desc_out = self.nlp_act(offer_desc_out)
        offer_desc_out = self.search_nlp_dense_1(offer_desc_out)
        offer_desc_out = self.nlp_act(offer_desc_out)

        user_ctx_out = self.user_context_head(deep_in=user_deep_in, wide_in=user_wide_in)
        user_out = torch.cat([search_out, aep_seq_out, svc_out, new_svc_out, user_ctx_out], dim=1)
        user_out = self.user_dense_0(user_out)
        user_out = self.user_act(user_out)
        user_out = self.user_dropout(user_out)
        user_out = self.user_dense_1(user_out)
        user_out = self.user_act(user_out)

        offer_ctx_out = self.offer_context_head(deep_in=offer_deep_in, wide_in=offer_wide_in)
        offer_out = torch.cat([offer_ctx_out, offer_desc_out])
        offer_out = self.offer_dense_0(offer_out)
        offer_out = self.offer_act(offer_out)
        offer_out = self.offer_dropout(offer_out)
        offer_out = self.offer_dense_1(offer_out)
        offer_out = self.offer_act(offer_out)

        out = torch.mul(user_out, offer_out)
        out = torch.sum(out, dim=1)
        out = self.out_act(out)

        return out, user_out, offer_out


class BSTAudienceTwoTowerPplan(nn.Module):
    def __init__(self, user_deep_dims, user_deep_embed_dims, user_num_wide, user_num_shared, user_wad_embed_dim,
                 offer_deep_dims, offer_deep_embed_dims, offer_num_wide, offer_num_shared, offer_wad_embed_dim,
                 svc_dim, svc_embed_dim, page_dim, page_embed_dim, item_dim, item_embed_dim, seq_embed_dim,
                 seq_hidden_size,
                 nlp_encoder_path, nlp_dim=0, sequence_transformer_kwargs=None):
        super().__init__()
        # user layers
        self.user_context_head = ContextHead(
            deep_dims=user_deep_dims,
            num_wide=user_num_wide,
            deep_embed_dims=user_deep_embed_dims,
            wad_embed_dim=user_wad_embed_dim,
            num_shared=user_num_shared,
        )

        self.svc_embedding = nn.Embedding(svc_dim, svc_embed_dim)
        self.svc_pooling = MeanMaxPooling()

        self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        self.item_embedding = nn.Embedding(item_dim, item_embed_dim)
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )

        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        self.search_nlp_dense_0 = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=seq_embed_dim * 2
        )
        self.search_nlp_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim // 2
        )
        self.nlp_act = nn.LeakyReLU(0.2)

        if user_num_wide:
            user_ctx_out_dims = user_wad_embed_dim
        else:
            user_ctx_out_dims = user_wad_embed_dim // 2
        self.user_dense_0 = torch.nn.Linear(
            # nlp_out + aep_seq_out + svc_out + user_ctx_out
            in_features=seq_embed_dim // 2 + seq_embed_dim + svc_embed_dim * 2 + user_ctx_out_dims,
            out_features=seq_embed_dim * 2
        )
        self.user_dense_1 = torch.nn.Linear(
            in_features=seq_embed_dim * 2,
            out_features=seq_embed_dim
        )
        self.user_act = nn.LeakyReLU(0.2)
        self.user_dropout = nn.Dropout(p=0.1)

        # offer layers
        self.offer_context_head = ContextHead(
            deep_dims=offer_deep_dims,
            num_wide=offer_num_wide,
            deep_embed_dims=offer_deep_embed_dims,
            wad_embed_dim=offer_wad_embed_dim,
            num_shared=offer_num_shared,
        )

        if offer_num_wide:
            offer_ctx_out_dims = offer_wad_embed_dim
        else:
            offer_ctx_out_dims = offer_wad_embed_dim // 2
        self.offer_dense_0 = torch.nn.Linear(
            in_features=offer_ctx_out_dims,
            out_features=offer_ctx_out_dims + offer_ctx_out_dims // 2
        )
        self.offer_dense_1 = torch.nn.Linear(
            in_features=offer_ctx_out_dims + offer_ctx_out_dims // 2,
            out_features=seq_embed_dim
        )
        self.offer_act = nn.LeakyReLU(0.2)
        self.offer_dropout = nn.Dropout(p=0.1)

        self.out_act = nn.Sigmoid()

    def forward(self, user_deep_in, offer_deep_in, svc_in, page_in, item_in, vl_in,
                user_wide_in=None, offer_wide_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        svc_out = self.svc_embedding(svc_in.long())
        svc_out = self.svc_pooling(svc_out)

        aep_seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)

        search_out = self.nlp_encoder(**search_in).last_hidden_state[:, 0, :].to(dtype=torch.float32)
        search_out = self.search_nlp_dense_0(search_out)
        search_out = self.nlp_act(search_out)
        search_out = self.search_nlp_dense_1(search_out)
        search_out = self.nlp_act(search_out)

        user_ctx_out = self.user_context_head(deep_in=user_deep_in, wide_in=user_wide_in)
        user_out = torch.cat([search_out, aep_seq_out, svc_out, user_ctx_out], dim=1)
        user_out = self.user_dense_0(user_out)
        user_out = self.user_act(user_out)
        user_out = self.user_dropout(user_out)
        user_out = self.user_dense_1(user_out)
        user_out = self.user_act(user_out)

        offer_ctx_out = self.offer_context_head(deep_in=offer_deep_in, wide_in=offer_wide_in)
        offer_out = offer_ctx_out
        offer_out = self.offer_dense_0(offer_out)
        offer_out = self.offer_act(offer_out)
        offer_out = self.offer_dropout(offer_out)
        offer_out = self.offer_dense_1(offer_out)
        offer_out = self.offer_act(offer_out)

        out = torch.mul(user_out, offer_out)
        out = torch.sum(out, dim=1)
        out = self.out_act(out)

        return out, user_out, offer_out


class BSTAudienceCandidate(BST):
    def __init__(self, offer_num, deep_dims, page_dim, seq_dim, page_embed_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size,
                 nlp_encoder_path, num_wide=0, num_shared=0, nlp_dim=0, context_head_kwargs=None,
                 sequence_transformer_kwargs=None, page_embedding_weight=None, item_embedding_weight=None,
                 shared_embeddings_weight=None):
        super().__init__(deep_dims, seq_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size,
                         num_wide, num_shared, nlp_dim, context_head_kwargs, sequence_transformer_kwargs,
                         item_embedding_weight, shared_embeddings_weight)
        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        self.offer_num = offer_num

        if page_embedding_weight is None:
            print("not use pretrained embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained item embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)

        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )
        self.dense_out = torch.nn.Linear(seq_embed_dim, self.offer_num)
        self.act_out = nn.Softmax()

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, shared_in=None,
                search_ids=None, att_mask=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(search_ids, att_mask).last_hidden_state[:, 0, :].to(dtype=torch.float32)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense_out(user_out)
        outs = self.act_out(outs)
        return outs, user_out
    
    
class BSTHome(nn.Module):
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, deep_embed_dims, wad_embed_dim, nlp_embed_dim, seq_hidden_size, nlp_encoder_path, freeze=False,
                 num_wide=0, num_shared=0, nlp_dim=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 page_embedding_weight=None, item_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__()
        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        
        if freeze:
            for param in self.nlp_encoder.parameters():
                param.requires_grad = False
        
        context_head_kwargs = context_head_kwargs if context_head_kwargs else {}
        sequence_transformer_kwargs = sequence_transformer_kwargs if sequence_transformer_kwargs else {}
        
        if page_embedding_weight is None:
            print("not use pretrained embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained item embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)

        if item_embedding_weight is None:
            print("not use pretrained embedding")
            self.item_embedding = nn.Embedding(seq_dim, item_embed_dim)
        else:
            print("use pretrained item embedding")
            self.item_embedding = nn.Embedding.from_pretrained(item_embedding_weight, freeze=False)
            
        self.context_head = ContextHead(
            deep_dims=deep_dims,
            num_wide=num_wide,
            item_embedding=self.item_embedding,
            shared_embeddings_weight=shared_embeddings_weight,
            wad_embed_dim=wad_embed_dim,
            deep_embed_dims=deep_embed_dims
        )
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=page_embed_dim + item_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )
        self.seq_dense = torch.nn.Linear(
            in_features=page_embed_dim + item_embed_dim,
            out_features=seq_embed_dim
        )
        self.nlp_dense = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=nlp_embed_dim
        )
        self.dense1 = torch.nn.Linear(
            in_features=nlp_embed_dim + wad_embed_dim + seq_embed_dim,
            out_features=seq_embed_dim)
        self.act1 = self.act2 = nn.LeakyReLU(0.2)
        self.dense2 = torch.nn.Linear(seq_embed_dim, seq_embed_dim // 2)
        self.dense3 = torch.nn.Linear(seq_embed_dim // 2, 1)

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, shared_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(**search_in).last_hidden_state[:,0,:].to(dtype=torch.float32)
        search_out = self.nlp_dense(search_out)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)
        seq_out = self.seq_dense(seq_out)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        outs = self.act2(outs)
        outs = self.dense3(outs)
        return outs
    
    
class BSTGridwall(nn.Module):
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, deep_embed_dims, wad_embed_dim, nlp_embed_dim, seq_hidden_size, nlp_encoder_path, 
                 num_wide=0, num_shared=0, nlp_dim=0, item_freeze=None, nlp_freeze=None, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 page_embedding_weight=None, item_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__()
        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)
        context_head_kwargs = context_head_kwargs if context_head_kwargs else {}
        sequence_transformer_kwargs = sequence_transformer_kwargs if sequence_transformer_kwargs else {}
        
        if page_embedding_weight is None:
            print("not use pretrained embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained item embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)

        if item_embedding_weight is None:
            print("not use pretrained embedding")
            self.item_embedding = nn.Embedding(seq_dim, item_embed_dim)
        else:
            print("use pretrained item embedding")
            self.item_embedding = nn.Embedding.from_pretrained(item_embedding_weight, freeze=False)
            
        if item_freeze:
            self.item_embedding.weight.requires_grad = False
            
        if nlp_freeze:
            for param in self.nlp_encoder.parameters():
                param.requires_grad = False
            
        self.context_head = ContextHead(
            deep_dims=deep_dims,
            num_wide=num_wide,
            item_embedding=self.item_embedding,
            shared_embeddings_weight=shared_embeddings_weight,
            wad_embed_dim=wad_embed_dim,
            deep_embed_dims=deep_embed_dims
        )
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=page_embed_dim + item_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )
        self.seq_dense = torch.nn.Linear(
            in_features=page_embed_dim + item_embed_dim,
            out_features=seq_embed_dim
        )
        self.nlp_dense = torch.nn.Linear(
            in_features=nlp_dim,
            out_features=nlp_embed_dim
        )
        self.dense1 = torch.nn.Linear(
            in_features=nlp_embed_dim + wad_embed_dim + seq_embed_dim,
            out_features=seq_embed_dim)
        self.act1 = self.act2 = nn.LeakyReLU(0.2)
        self.dense2 = torch.nn.Linear(seq_embed_dim, seq_embed_dim)
        self.dense3 = torch.nn.Linear(seq_embed_dim, seq_dim)

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, input_ids=None, attention_mask=None, shared_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state[:,0,:].to(dtype=torch.float32)
        search_out = self.nlp_dense(search_out)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)
        seq_out = self.seq_dense(seq_out)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense3(user_out)
        return (outs, user_out)


class BSTCanGen(BST):
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, item_embed_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size, nlp_encoder_path, 
                 num_wide=0, num_shared=0, nlp_dim=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 page_embedding_weight=None, item_embedding_weight=None, shared_embeddings_weight=None):
        # super(BSTBottom, self).__init__()
        super().__init__(deep_dims, seq_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size, nlp_encoder_path, 
                         num_wide, num_shared, nlp_dim, context_head_kwargs, sequence_transformer_kwargs,
                         item_embedding_weight, shared_embeddings_weight)
        self.nlp_encoder = DistilBertModel.from_pretrained(nlp_encoder_path)

        # config = DistilBertConfig.from_json_file(nlp_encoder_path)
        # self.nlp_encoder = DistilBertModel(config)
        
        if page_embedding_weight is None:
            print("not use pretrained embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained item embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)

        if item_embedding_weight is None:
            print("not use pretrained embedding")
            self.item_embedding = nn.Embedding(seq_dim, item_embed_dim)
        else:
            print("use pretrained item embedding")
            self.item_embedding = nn.Embedding.from_pretrained(item_embedding_weight, freeze=True)
        
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            page_embed_dim=page_embed_dim,
            item_embed_dim=item_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )

        self.context_head = ContextHead(
            deep_dims=deep_dims,
            num_wide=num_wide,
            item_embedding=self.item_embedding,
            # seq_embed_dim=seq_embed_dim,
            shared_embeddings_weight=shared_embeddings_weight,
            deep_embed_dims=deep_embed_dims
        )

        # self.nlp_dense = torch.nn.Linear(
        #     in_features=nlp_dim,
        #     out_features=seq_embed_dim
        # )
        # self.dense1 = torch.nn.Linear(
        #     in_features=seq_embed_dim * 2+len(deep_dims)*deep_embed_dims+num_wide+seq_embed_dim+seq_embed_dim+(num_shared*seq_embed_dim),
        #     out_features=2 * seq_embed_dim
        # )
        self.dense3 = torch.nn.Linear(seq_embed_dim, seq_dim)

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, shared_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(**search_in).last_hidden_state[:,0,:].to(dtype=torch.float32)
        search_out = self.nlp_dense(search_out)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)

        ## search_out, offer_desc_out, offer_ctx_out, seq_out, user_ctx_out 
        ## search_out + seq_out + user_ctx_out -> user_dense
        ## offer_desc_out + offer_ctx_out -> offer_dense
        ## outs, user_dense
        ## seed 100k (600 attributes) -> aug 1 mil (600 attributes)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense3(user_out)
        return (outs, user_out)


class BSTCanGenInference(BST):
    def __init__(self, deep_dims, page_dim, seq_dim, page_embed_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size, nlp_encoder_path, 
                 num_wide=0, num_shared=0, nlp_dim=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 page_embedding_weight=None, item_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__(deep_dims, seq_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size,
                         num_wide, num_shared, nlp_dim, context_head_kwargs, sequence_transformer_kwargs,
                         item_embedding_weight, shared_embeddings_weight)
        config = DistilBertConfig.from_json_file(nlp_encoder_path)
        self.nlp_encoder = DistilBertModel(config)
        if page_embedding_weight is None:
            print("not use pretrained embedding")
            self.page_embedding = nn.Embedding(page_dim, page_embed_dim)
        else:
            print("use pretrained item embedding")
            self.page_embedding = nn.Embedding.from_pretrained(page_embedding_weight, freeze=True)
        
        self.sequence_transformer = SequenceTransformerAEP(
            page_embedding=self.page_embedding,
            item_embedding=self.item_embedding,
            seq_embed_dim=seq_embed_dim,
            seq_hidden_size=seq_hidden_size,
            **sequence_transformer_kwargs,
        )
        self.dense3 = torch.nn.Linear(seq_embed_dim, seq_dim)

    def forward(self, deep_in, page_in, item_in, vl_in, wide_in=None, shared_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(**search_in).last_hidden_state[:,0,:].to(dtype=torch.float32)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(page_in=page_in, item_in=item_in, vl_in=vl_in)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense3(user_out)
        return (outs, user_out)


class BSTBERTInference(BST):
    def __init__(self, deep_dims, seq_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size, nlp_encoder_path,
                 num_wide=0, num_shared=0, nlp_dim=0, context_head_kwargs=None, sequence_transformer_kwargs=None,
                 item_embedding_weight=None, shared_embeddings_weight=None):
        super().__init__(deep_dims, seq_dim, seq_embed_dim, deep_embed_dims, seq_hidden_size,
                         num_wide, num_shared, nlp_dim, context_head_kwargs, sequence_transformer_kwargs,
                         item_embedding_weight, shared_embeddings_weight)
        self.nlp_encoder = AutoModel.from_pretrained(nlp_encoder_path)
        self.dense3 = torch.nn.Linear(seq_embed_dim, seq_dim)

    def forward(self, deep_in, seq_in, vl_in, wide_in=None, shared_in=None, search_in=None):
        """
        Args:
            deep_in: list, a list of Tensor of shape [batch_size, deep_dims].
            seq_in: Tensor, shape [batch_size, seq_len].
            vl_in: Tensor, shape [batch_size].
            wide_in: list, a list of Tensor of shape [batch_size, num_wide].
            shared_in: list, a list of Tensor of shape [batch_size, num_shared] (default=None).
            search_ids: tensor, Tensor of shape [batch_size, sentence_length] (default=None).
            att_mask: tensor, Tensor of shape [batch_size, sentence_length] (default=None).

        Return:
            out: Tensor, shape [batch_size, seq_dim].
            user_out: Tensor, shape [batch_size, seq_embed_dim].
        """
        search_out = self.nlp_encoder(**search_in).last_hidden_state[:,0,:].to(dtype=torch.float32)
        ctx_out = self.context_head(deep_in=deep_in, wide_in=wide_in, shared_in=shared_in)
        seq_out = self.sequence_transformer(seq_in=seq_in, vl_in=vl_in)
        outs = torch.cat([seq_out, ctx_out, search_out], dim=1)
        outs = self.dense1(outs)
        outs = self.act1(outs)
        outs = self.dense2(outs)
        user_out = self.act2(outs)
        outs = self.dense3(user_out)
        return (outs, user_out)