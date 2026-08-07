from __future__ import annotations

from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class TenantModel(Base):

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    leases: Mapped[list["LeaseModel"]] = relationship(
        back_populates="tenant",
        cascade="all, delete-orphan"
    )


class PropertyModel(Base):

    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    province: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    postal_code: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    leases: Mapped[list["LeaseModel"]] = relationship(
        back_populates="property",
        cascade="all, delete-orphan"
    )


class LeaseModel(Base):

    __tablename__ = "leases"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey(
            "tenants.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    property_id: Mapped[int] = mapped_column(
        ForeignKey(
            "properties.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    monthly_rent: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    tenant: Mapped["TenantModel"] = relationship(
        back_populates="leases"
    )

    property: Mapped["PropertyModel"] = relationship(
        back_populates="leases"
    )

    payments: Mapped[list["PaymentModel"]] = relationship(
        back_populates="lease",
        cascade="all, delete-orphan"
    )


class PaymentModel(Base):

    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    lease_id: Mapped[int] = mapped_column(
        ForeignKey(
            "leases.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    payment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    reference: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    lease: Mapped["LeaseModel"] = relationship(
        back_populates="payments"
    )